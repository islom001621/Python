#1
avg_grade=df1[['Math','English','Science']].mean()

print(avg_grade)


#2
df1["Average"]=df1[['Math','English','Science']].mean(axis=1)

top_student=df1.loc[df1["Average"].idxmax()]

print(top_student)


#3
df1["Total"]=df1[['Math','English','Science']].sum(axis=1)

print(df1)



#4
category = df1.columns
values=df1.mean()

bar = plt.bar(category,values,0.5,color=['skyblue','red','green'])
bar


#1

total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print(total_sales)

#2
df2['Total'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)

max_sales_date = df2.loc[df2['Total'].idxmax(), 'Date']
print("Date with highest total sales:", max_sales_date)

max_sales_date

#3
pct_change_df = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100


df2['Product_A_pct_change'] = pct_change_df['Product_A']
df2['Product_B_pct_change'] = pct_change_df['Product_B']
df2['Product_C_pct_change'] = pct_change_df['Product_C']


df2


#4

import matplotlib.pyplot as plt

# Set the figure size
plt.figure(figsize=(10, 6))

# Plot each product's sales over time
plt.plot(df2['Date'], df2['Product_A'], label='Product A', marker='o')
plt.plot(df2['Date'], df2['Product_B'], label='Product B', marker='s')
plt.plot(df2['Date'], df2['Product_C'], label='Product C', marker='^')

# Add titles and labels
plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()

#1
f=df3.groupby("Department")['Salary'].mean()

print(f)


#2

top_employee=df3.loc[df3['Experience (Years)'].idxmax()]

print(top_employee)


#3
min_salary = df3['Salary'].min()


df3['Salary Increase']=((df3['Salary']-min_salary)/ min_salary)*100

print(df3)

#4
import matplotlib.pyplot as plt

# Count employees per department
department_counts = df3['Department'].value_counts()

# Plot the bar chart
plt.figure(figsize=(8, 5))
plt.bar(department_counts.index, department_counts.values, color='skyblue', edgecolor='black')

plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#1
total_revenue = df4['Quantity'] * df4['Total_Price']

print(total_revenue)
#2
average_quantity = df4['Quantity'].mean()
print("Average quantity of products ordered:", average_quantity)


#3
product_orders=df4.groupby('Product')['Quantity'].sum()

most_ordered_product=product_orders.idxmax()
most_ordered_quantity = product_orders.max()

print(f"The most ordered product is '{most_ordered_product}' with {most_ordered_quantity} units.")


#4
sales_by_product = df4.groupby('Product')['Total_Price'].sum()

# Plot the pie chart
plt.figure(figsize=(7, 7))
plt.pie(sales_by_product, labels=sales_by_product.index, autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution by Product')
plt.axis('equal')  # Equal aspect ratio ensures a circular pie
plt.show()
