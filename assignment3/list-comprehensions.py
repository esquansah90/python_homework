#Task3

import csv

employees = []

with open("../csv/employees.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        employees.append(row)

names = [f"{row[0]} {row[1]}" for row in employees[1:]]
print("All employee names:")
print(names)

names_with_e = [name for name in names if "e" in name.lower()]
print("\nNames containing the letter 'e':")
print(names_with_e)
