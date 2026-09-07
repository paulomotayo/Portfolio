import csv
from operator import itemgetter


def main():
    with open("transactions.csv", "r") as file:
        reader = csv.DictReader(file)

        total, by_category, by_customer = process_reader(reader)

    print(f"\nTotal revenue: {total:.2f}\n")
    print("Revenue by category\n")
    
    for key, value in sorted(by_category.items(), key=itemgetter(1), reverse=True):
        print(f"{key:<15}: {value:.2f}")

    if not by_customer:
        raise ValueError("No valid transactions found")
    
    top_customer = max(by_customer.items(), key=itemgetter(1))

    print(f"\nTop customer is {top_customer[0].capitalize()} and they spent ${top_customer[1]:.0f}")


def process_reader(reader):
    total, by_category, by_customer = 0, {}, {}

    for line in reader:
        try:
            amount = float(line["amount"])
        except ValueError:
            continue

        category = line["category"].lower().strip()

        if amount < 0 or not line["customer"] or not line["category"]:
            continue

        customer = line["customer"].lower().strip()

        by_category[category] = by_category.get(category, 0.0) + amount
        by_customer[customer] = by_customer.get(customer, 0.0) + amount

        total += amount

    return total, by_category, by_customer


if __name__ == "__main__":
    main()