import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the survey data from CSV
data = pd.read_csv('survey_data.csv')

# Data Visualization
plt.figure(figsize=(18, 12))

# Age Group Distribution
plt.subplot(2, 2, 1)
data['age_group'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Age Group Distribution')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.xticks(rotation=0)

# Gender Distribution
plt.subplot(2, 2, 2)
data['gender'].value_counts().plot(kind='bar', color='lightgreen')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)

# Preferred Social Media Platform
plt.subplot(2, 2, 3)
data['social_media_platform'].value_counts().plot(kind='bar', color='salmon')
plt.title('Preferred Social Media Platform')
plt.xlabel('Platform')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')

# Cultural Comfort Distribution
plt.subplot(2, 2, 4)
data['cultural_comfort'].value_counts().plot(kind='bar', color='orange')
plt.title('Cultural Comfort Distribution')
plt.xlabel('Cultural Comfort')
plt.ylabel('Count')
plt.xticks(rotation=0)

plt.tight_layout()  # Adjust layout to prevent overlapping

plt.show()
