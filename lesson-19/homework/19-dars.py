#1
df=df.groupby('Category').agg({'Quantity':['sum','max'],"Price":'mean'})

#1.2
product_sales = df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()


top_products = product_sales.sort_values(['Category', 'Quantity'], ascending=[True, False]) \
                            .drop_duplicates(subset='Category', keep='first')

print(top_products)

1.3
df['TotalSales'] = df['Quantity'] * df['Price']

# 2. Sanaga qarab jami savdoni hisoblash
daily_sales = df.groupby('Date')['TotalSales'].sum().reset_index()

# 3. Eng yuqori savdo bo‘lgan sanani topish
max_sales_date = daily_sales.loc[daily_sales['TotalSales'].idxmax()]


# Step 1: Group by CustomerID and count the number of orders
order_counts = customer.groupby('CustomerID').size()

# Step 2: Filter CustomerIDs with 20 or more orders
valid_customers = order_counts[order_counts >= 20].index

# Step 3: Filter the original DataFrame
filtered_df = customer[customer['CustomerID'].isin(valid_customers)]

# Display the result
print(filtered_df)


# Har bir CustomerID bo‘yicha o‘rtacha narxni hisoblash
avg_price = customer.groupby('CustomerID')['Price'].mean().reset_index()

# $120 dan katta bo‘lganlarni tanlash
high_spenders = avg_price[avg_price['Price'] > 120]

# Asl jadvaldan faqat shu mijozlarga tegishli buyurtmalarni olish
filtered_data = customer[customer['CustomerID'].isin(high_spenders['CustomerID'])]

print(filtered_data)


product_summary = customer.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_price=('Price', lambda x: (x * customer.loc[x.index, 'Quantity']).sum())
).reset_index()

# 5 donadan kam sotilgan mahsulotlarni filtrdan o‘tkazish
filtered_products = product_summary[product_summary['total_quantity'] >= 5]

print(filtered_products)



import pandas as pd
import sqlite3

# --- STEP 1: Fayllarni yuklash ---
# 1.1 Excel fayldan salary band toifalarini yuklash
salary_band_df = pd.read_excel("C:\\Users\\user\\Downloads\\population_salary_analysis.xlsx")

# 1.2 SQLite dan population jadvalini o‘qish
conn = sqlite3.connect("C:\\Users\\user\\Downloads\\population.db")
population_df = pd.read_sql_query("SELECT * FROM population", conn)

# --- STEP 2: Salary Band ni aniqlash ---
def assign_salary_band(salary):
    for _, row in salary_band_df.iterrows():
        if row['Min Salary'] <= salary <= row['Max Salary']:
            return row['Band']
    return 'Unknown'

population_df['Salary Band'] = population_df['salary'].apply(assign_salary_band)

# --- STEP 3: Umumiy statistikalar ---
total_population = len(population_df)

salary_band_stats = population_df.groupby('Salary Band').agg(
    Population_Count=('Salary', 'count'),
    Average_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median')
).reset_index()

salary_band_stats['Percentage'] = (salary_band_stats['Population_Count'] / total_population * 100).round(2)

# --- STEP 4: Har bir shtat bo‘yicha statistikalar ---
state_salary_stats = population_df.groupby(['State', 'Salary Band']).agg(
    Population_Count=('Salary', 'count'),
    Average_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median')
).reset_index()

# Ulushini hisoblash uchun har bir State bo‘yicha umumiy sonni topamiz
state_total = population_df.groupby('State')['Salary'].count().reset_index(name='State_Total')

# Qo‘shamiz
state_salary_stats = state_salary_stats.merge(state_total, on='State')
state_salary_stats['Percentage'] = (state_salary_stats['Population_Count'] / state_salary_stats['State_Total'] * 100).round(2)

# Faqat kerakli ustunlar
state_salary_stats = state_salary_stats[['State', 'Salary Band', 'Population_Count', 'Average_Salary', 'Median_Salary', 'Percentage']]

# --- STEP 5: Natijalarni ko‘rsatish ---
print("== Salary Band Statistics (Overall) ==")
print(salary_band_stats)

print("\n== Salary Band Statistics per State ==")
print(state_salary_stats)
