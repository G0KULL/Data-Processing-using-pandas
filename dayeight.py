import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('sales_data.csv')
df['Total Price']=df['Unit Price']* df['Units Sold']

print('\n--First five details --')
print(df.head())

sales_by_product = df.groupby('Product')['Total Price'].sum()
print('\nTotal price based on Product')
print(sales_by_product)

plt.figure(figsize=(6,4))
sns.barplot(x=sales_by_product.index,y=sales_by_product.values,palette='Greens_d')
plt.title('Total price of Products')
plt.ylabel('Sales Amount $')
plt.show()