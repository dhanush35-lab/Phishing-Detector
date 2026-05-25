# Phishing Website Detector

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-6A737D.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2+-F7931E.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-1.7+-665191.svg)

A comprehensive phishing website detection system using Machine Learning. This project combines advanced web scraping, feature engineering, and gradient boosting models to identify malicious URLs with high accuracy.

## Features

- **Advanced URL Analysis**: Extracts lexical, domain, and content-based features from URLs
- **WHOIS Integration**: Checks domain registration age and registrar information
- **Machine Learning Detection**:
  - **Random Forest** - Fast baseline model
  - **XGBoost** - High-performance gradient boosting
  - **Ensemble Voting** - Combines multiple models for superior accuracy
- **Explainable AI**: Uses **SHAP** to explain model predictions
- **Real-time API**: Flask-based API for easy integration
- **Modern Interface**: Clean, responsive web interface

## Tech Stack

- **Backend**: Python 3.11+, Flask, Flask-CORS
- **Machine Learning**: Scikit-learn, XGBoost, SHAP, NumPy, Pandas
- **Web Scraping**: Requests, Beautiful Soup, python-whois
- **Frontend**: HTML, CSS, JavaScript (Vanilla)

## Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Phishing-Detector
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Start the Server

```bash
python app.py
```

The server will start at `http://[IP_ADDRESS]`.

### Test the API

**Check a URL (POST):**
```bash
curl -X POST http://[IP_ADDRESS]/predict -H "Content-Type: application/json" -d '{"url": "https://www.google.com"}'
```

**Get Feature Importances (GET):**
```bash
curl http://[IP_ADDRESS]/feature_importances
```

## Project Structure

```
Phishing-Detector/
├── models/                # Trained ML models and scalers
├── data/                  # Datasets
│   ├── test_urls.csv
│   ├── train_urls.csv
│   └── updated_dataset.csv
├── templates/             # HTML templates
│   └── index.html
├── app.py                 # Flask application and API
├── features.py            # Feature engineering
├── phishing_detector.ipynb  # Jupyter notebook experiments
└── requirements.txt       # Dependencies
```

## Models

### Model Files

The `models/` directory contains:
- `ensemble_model.pkl`: Final ensemble model
- `random_forest_model.pkl`: Random Forest classifier
- `xgboost_model.pkl`: XGBoost classifier
- `scaler.pkl`: StandardScaler for feature scaling

### Feature Engineering

The `features.py` module extracts 30+ features including:
- **Lexical Features**: URL length, word count, special character ratio
- **Domain Features**: Domain length, presence of IP address, TLD verification
- **Content Features**: Presence of suspicious keywords, HTML length
- **External Features**: WHOIS registration age, SSL certificate status

## Training

To retrain the models with new data:

1. Update the dataset in `data/`
2. Run the Jupyter notebook or training scripts
3. The models will be saved to `models/`

## Development

### Environment

It's recommended to use the provided virtual environment. To deactivate:
```bash
deactivate
```

### Adding New Features

1. Update `features.py` with the new feature extraction logic
2. Update `phishing_detector.ipynb` to test the new feature
3. Retrain the models
4. Update `requirements.txt` if new libraries are needed

## License

This project is licensed under the MIT License.

Built with ❤️ by Deon George | Dhanush M


