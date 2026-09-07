# ETL Revenue Analyzer

A small Python ETL project that reads transaction data from a CSV file, filters out invalid records, and generates a revenue report.

## Features

- Reads transaction data using `csv.DictReader`
- Ignores invalid transactions
- Calculates total revenue
- Aggregates revenue by category and by customer
- Finds the top customer
- Sorts categories by revenue

## Files

- `transactions.csv` - sample transaction data
- `etl_revenue_analyzer.py` - main program

## Example Output

```text

Total revenue: 10455.74

Revenue by category

food           : 3725.00
shopping       : 2500.50
transport      : 625.00

Top customer is Alice and they spent $1525