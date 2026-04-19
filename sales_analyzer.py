import pandas as pd

# EXTRACT
df = pd.read_excel("sales.xlsx")

# Convert Date
df['Date'] = pd.to_datetime(df['Date'])

# Extract Year
df['Year'] = df['Date'].dt.year

# TRANSFORM: Group data
grouped = df.groupby(['Year', 'Customer_Name'])['Sales_Amount'].sum().reset_index()

print("\nGrouped Data:")
print(grouped)
# SORT by Year and Sales descending
grouped_sorted = grouped.sort_values(['Year', 'Sales_Amount'], ascending=[True, False])

print("\nSorted Data:")
print(grouped_sorted)

# Get Top 50 customers per year
top_customers = grouped_sorted.groupby('Year').head(50)

print("\nTop Customers Per Year:")
print(top_customers)


final_result = []

previous_top_customers = set()

years = sorted(grouped_sorted['Year'].unique())

for year in years:
    current_year_data = grouped_sorted[grouped_sorted['Year'] == year]

    # Current top 50
    current_top = current_year_data.head(50)

    # Create DataFrame for previous customers (even if missing)
    prev_customers_list = list(previous_top_customers)

    prev_df = pd.DataFrame({
        'Year': year,
        'Customer_Name': prev_customers_list
    })

    # Merge with actual data to get Sales_Amount
    prev_df = prev_df.merge(current_year_data, on=['Year', 'Customer_Name'], how='left')

    # Fill missing sales with 0
    prev_df['Sales_Amount'] = prev_df['Sales_Amount'].fillna(0)

    # Combine
    combined = pd.concat([current_top, prev_df]).drop_duplicates(subset=['Customer_Name'])

    # Update previous customers
    previous_top_customers.update(combined['Customer_Name'])

    final_result.append(combined)

# Final output
final_df = pd.concat(final_result)

print("\nFinal Result:")
print(final_df)