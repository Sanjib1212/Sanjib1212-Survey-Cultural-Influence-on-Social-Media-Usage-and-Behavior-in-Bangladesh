import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV dataset
data = pd.read_csv('survey_data.csv')

# Display the first few rows of the dataset to understand its structure
print(data.head())
# Define the order of age groups for consistent plotting
age_order = [
    'Child (Under 18)',
    'Young Adult (18-34)',
    'Middle-aged (35-54)',
    'Older (55+)',
]

# Create a pivot table to summarize adherence to cultural norms by age group
pivot_table = data.pivot_table(index='age_group', columns='cultural_norm', aggfunc='size', fill_value=0)

# Normalize the counts to show percentages across each age group
pivot_table_percent = pivot_table.div(pivot_table.sum(axis=1), axis=0) * 100

# Plotting the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_table_percent.loc[age_order], annot=True, cmap='Blues', fmt='.1f', cbar=True)
plt.title('Privacy Settings Based on Cultural Norms by Age Group')
plt.xlabel('Cultural Norm')
plt.ylabel('Age Group')
plt.tight_layout()
plt.show()
