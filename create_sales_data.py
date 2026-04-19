import pandas as pd

data = {
    "Customer_Name": [
        "Ali", "John", "Sara", "Ali", "John", "Sara",
        "Khan", "Meena", "Ali", "John"
    ],
    "Date": [
        "2022-01-10", "2022-02-15", "2022-03-20",
        "2023-01-12", "2023-04-18", "2023-05-22",
        "2023-06-10", "2023-07-14", "2024-01-11", "2024-03-05"
    ],
    "Sales_Amount": [
        100, 200, 150, 300, 250, 180,
        400, 350, 500, 600
    ]
}

df = pd.DataFrame(data)

df.to_excel("sales.xlsx", index=False)

print("sales.xlsx file created successfully!")