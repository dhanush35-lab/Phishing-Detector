from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
from explainability import PhishingExplainer

# Import your custom files
from featureextraction import extract_features


# -----------------------------
# Initialize Flask App
# -----------------------------
app = Flask(__name__)
CORS(app)

# -----------------------------
# Load Trained Model
# -----------------------------
model = pickle.load(open("phishing_model.pkl", "rb"))

# -----------------------------
# Feature Names
# (same order used during training)
# -----------------------------
feature_names = [
    'having_IP_Address',
    'URL_Length',
    'Shortining_Service',
    'having_At_Symbol',
    'double_slash_redirecting',
    'Prefix_Suffix',
    'having_Sub_Domain',
    'SSLfinal_State'
]

# -----------------------------
# Initialize Explainer
# -----------------------------
explainer = PhishingExplainer(model, feature_names)

# -----------------------------
# Home Route
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "Phishing Detection API is running"
    })

# -----------------------------
# Prediction Route
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get URL from frontend
        data = request.get_json()

        if "url" not in data:
            return jsonify({
                "error": "URL not provided"
            }), 400

        url = data["url"]

        # -----------------------------
        # Feature Extraction
        # -----------------------------
        features = extract_features(url)

        # Convert into numpy array
        features_array = np.array(features).reshape(1, -1)

        # -----------------------------
        # Prediction
        # -----------------------------
        prediction = model.predict(features_array)[0]

        # Probability
        probability = model.predict_proba(features_array)[0]

        confidence = round(max(probability) * 100, 2)

        # -----------------------------
        # Explainability
        # -----------------------------
        explanation = explainer.explain(features_array)

        # -----------------------------
        # Convert Prediction
        # -----------------------------
        if prediction == 1:
            result = "Legitimate"
        else:
            result = "Phishing"

        # -----------------------------
        # Final Response
        # -----------------------------
        response = {
            "url": url,
            "prediction": result,
            "confidence": confidence,
            "features": features,
            "explanation": explanation
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)