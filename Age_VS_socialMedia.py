import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the survey data from CSV
data = pd.read_csv('survey_data.csv')

# Create a pivot table to count the occurrences of each age group and social media platform combination
pivot_table = data.pivot_table(index='age_group', columns='social_media_platform', aggfunc='size', fill_value=0)

# Plotting the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_table, cmap='Blues', annot=True, fmt='d', linewidths=.5)
plt.title('Age Group vs Social Media Platform')
plt.xlabel('Social Media Platform')
plt.ylabel('Age Group')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.show()
