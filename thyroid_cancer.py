# -*- coding: utf-8 -*-
"""Thyroid_cancer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14nOMTSafN96yv-vH6eovQ_K8ngOls_T7
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('dataset.csv')

df.head()

df.info()

df

df.isnull().sum()

df['Adenopathy']

from sklearn.preprocessing import LabelEncoder

# Copy the dataset for preprocessing
df_cleaned = df.copy()

# List of binary categorical columns (Yes/No → 1/0)
binary_cols = ["Smoking", "Hx Smoking", "Hx Radiothreapy", "Adenopathy", "Recurred"]

# Convert binary categorical columns to numeric (Yes → 1, No → 0)
for col in binary_cols:
    df_cleaned[col] = df_cleaned[col].map({"Yes": 1, "No": 0})

# List of multi-category categorical columns
multi_cat_cols = ["Gender", "Thyroid Function", "Physical Examination",
                  "Pathology", "Focality", "Risk", "T", "N", "M", "Stage", "Response"]

# Apply Label Encoding
label_encoders = {}  # Store encoders for later use
for col in multi_cat_cols:
    le = LabelEncoder()
    df_cleaned[col] = le.fit_transform(df_cleaned[col])
    label_encoders[col] = le  # Save encoder

# Display cleaned dataset info
df_cleaned.info(), df_cleaned.head()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
file_path = "/mnt/data/dataset.csv"
df = pd.read_csv(file_path)

# Step 1: Inspect the data
df.info()
print("\nFirst 5 rows:")
print(df.head())

# Step 2: Data Cleaning & Preprocessing
# Convert binary categorical columns to numeric (Yes -> 1, No -> 0)
binary_cols = ["Smoking", "Hx Smoking", "Hx Radiothreapy", "Adenopathy", "Recurred"]
for col in binary_cols:
    df[col] = df[col].map({"Yes": 1, "No": 0})

# Apply Label Encoding to multi-category columns
multi_cat_cols = ["Gender", "Thyroid Function", "Physical Examination", "Pathology",
                  "Focality", "Risk", "T", "N", "M", "Stage", "Response"]
label_encoders = {}
for col in multi_cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Fill missing values in 'Adenopathy' with mode
df['Adenopathy'].fillna(df['Adenopathy'].mode()[0], inplace=True)

# Step 3: Exploratory Data Analysis (EDA)
# Target Variable Distribution
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Recurred", palette="Set2")
plt.title("Distribution of Thyroid Cancer Recurrence")
plt.show()

# Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Age"], bins=20, kde=True, color="blue")
plt.title("Age Distribution of Patients")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()

# Step 4: Feature Selection & Train-Test Split
X = df.drop(columns=["Recurred"])  # Features
y = df["Recurred"]  # Target variable

# Split data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Step 5: Model Training - Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Step 6: Model Evaluation
y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.2f}")
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)