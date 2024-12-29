import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('Dataset_Edited.csv')
original_dataset = pd.read_csv('student dropout.csv')

summary_stats = dataset.describe()
correlation_table = dataset.corr()
correlation_with_target = correlation_table["Dropped_Out"].sort_values(ascending=False)

print(summary_stats)
print(correlation_table)
print(correlation_with_target)

plt.figure(figsize=(20, 20))
sns.heatmap(correlation_table, annot=False, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.close()

plt.figure(figsize=(20, 20))
sns.histplot(dataset['Weighted_GPA_4.0'], kde=True, bins=20, color='blue')
plt.title("Distribution of Weighted GPA")
plt.xlabel("Weighted GPA")
plt.ylabel("Frequency")
plt.savefig("weighted_gpa_histogram.png")
plt.close()

plt.figure(figsize=(20, 20))
sns.boxplot(data=dataset, x="Dropped_Out", y="Number_of_Absences", palette="Set2")
plt.title("Number of Absences by Dropout Status")
plt.xlabel("Dropped Out (1 = Yes, 0 = No)")
plt.ylabel("Number of Absences")
plt.savefig("absences_boxplot.png")
plt.close()