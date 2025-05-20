import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Invoice.csv')



plt.figure(figsize=(10,5))
sns.histplot(df['Billing Amount (Rs.)'], bins=20, kde=True, color='teal')
plt.title('Distribution of Billing Amounts')
plt.xlabel('Billing Amount (Rs.)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()