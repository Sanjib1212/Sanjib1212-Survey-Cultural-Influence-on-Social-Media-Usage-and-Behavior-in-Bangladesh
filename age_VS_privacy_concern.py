import pandas as pd
import matplotlib.pyplot as plt

# Load the survey data from CSV
data = pd.read_csv('survey_data.csv')

# Display the first few rows of the dataset to understand its structure
print(data.head())
# Group the data by age_group and privacy_concern, and count the number of respondents in each group
age_privacy_counts = data.groupby(['age_group', 'privacy_concern']).size().unstack()

# Normalize the counts to get percentages within each age group
age_privacy_percentages = age_privacy_counts.div(age_privacy_counts.sum(axis=1), axis=0) * 100

# Plotting the bar chart
plt.figure(figsize=(12, 8))

# Plot each privacy concern category as a separate bar within each age group
age_privacy_percentages.plot(kind='bar', stacked=True)

# Customize the plot labels and title
plt.title('Privacy Concern by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45)
plt.legend(title='Privacy Concern', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
