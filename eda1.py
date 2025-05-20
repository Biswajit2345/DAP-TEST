import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Invoice.csv')

plt.figure(figsize=(8,5))
sns.countplot(data=df, y='Zone', order=df['Zone'].value_counts().index, palette='viridis')
plt.title('Distribution of Shipments by Zone')
plt.xlabel('Count')
plt.ylabel('Zone')
plt.grid(axis='x', linestyle='--')
plt.show()