# Sales Data Analyzer (ETL Project)

##  Project Overview
This project is a Python-based ETL pipeline that processes sales data from Excel files and generates structured reports.

##  Features
- Extract data from Excel
- Transform data using Pandas
- Group by year and customer
- Identify Top 50 customers per year
- Carry forward top customers to future years
- Include customers in later years even if no sales (filled with 0)
- Handle missing data 
- Export final results

##  Technologies Used
- Python
- Pandas
- Excel

##  Use Case
This project simulates real-world business requirements where historical top customers must be tracked over multiple years.

##  How to Run
1. Run `create_sales_data.py` to generate sample data
2. Run `sales_analyzer.py` to process data

##  Output
- Processed dataset with yearly top customers
