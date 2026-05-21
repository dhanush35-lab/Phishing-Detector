

import pandas as pd
import numpy as np

df = pd.read_csv("uci-ml-phishing-dataset.csv")

#print(df.head())

#print("\nDataset Shape:")
#print(df.shape)

#print("\nColumn Names:")
#print(df.columns)
#print(df.isnull().sum())
df = df.drop("id", axis=1)
X = df.drop("Result", axis=1)
y = df["Result"].replace(-1, 0)
#print(y.value_counts())
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
from xgboost import XGBClassifier
model = XGBClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import recall_score
recall = recall_score(y_test, y_pred)
print("Recall:", recall)
import joblib
joblib.dump(model, "phishing_model.pkl")
print(df.columns)