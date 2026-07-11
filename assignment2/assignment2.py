#Task2
import csv
import traceback

def read_employees():
    data = {}        
    rows = []        

    try:
        with open("../csv/employees.csv", "r") as f:
            reader = csv.reader(f)

            for index, row in enumerate(reader):
                if index == 0:
                    data["fields"] = row     
                else:
                    rows.append(row)       

        data["rows"] = rows
        return data

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )

        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()


employees = read_employees()

print(employees)


#Task3

def column_index(column_name):
    return employees["fields"].index(column_name)
employee_id_column = column_index("employee_id")

print("employee_id_column =", employee_id_column)

#Task4
def first_name(row_number):
    idx = column_index("first_name")
    row = employees["rows"][row_number]
    return row[idx]

print("First name at row 0:", first_name(0))

#Task5
def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))

    return matches

print("Find employee 1:", employee_find(1))

#Task6
def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id,
            employees["rows"]
        )
    )
    return matches

print("Find employee 1 (lambda):", employee_find_2(1))

#Task7
def sort_by_last_name():
    
    idx = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[idx])
    return employees["rows"]

print("Sorted by last name:")
print(sort_by_last_name())


#Task8
def employee_dict(row):
    result = {}

    for i in range(1, len(employees["fields"])):
        key = employees["fields"][i]
        value = row[i]
        result[key] = value

    return result

print("Employee dict for row 0:", employee_dict(employees["rows"][0]))

#Task9
def all_employees_dict():
    result = {}

    for row in employees["rows"]:
        emp_id = row[employee_id_column]
        result[emp_id] = employee_dict(row)

    return result

print("All employees dict:")
print(all_employees_dict())

#Task10
import os

def get_this_value():
    return os.getenv("THISVALUE")

print("Environment variable THISVALUE:", get_this_value())

#Task11

import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("I believe in unicorns!")

print(custom_module.secret)

#Task12
import csv

def read_minutes_file(filename):
    data = {}
    rows = []

    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)

            for index, row in enumerate(reader):
                if index == 0:
                    data["fields"] = row
                else:
                    rows.append(tuple(row))  

        data["rows"] = rows
        return data

    except Exception as e:
        print("Error reading:", filename)
        print(e)
        exit()


def read_minutes():
    minutes1 = read_minutes_file("../csv/minutes1.csv")
    minutes2 = read_minutes_file("../csv/minutes2.csv")
    return minutes1, minutes2


minutes1, minutes2 = read_minutes()

print("Minutes1:", minutes1)
print("Minutes2:", minutes2)

#Task13
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    combined = set1.union(set2)
    return combined

minutes_set = create_minutes_set()

print("Minutes Set:", minutes_set)


#Task14
from datetime import datetime

def create_minutes_list():
    lst = list(minutes_set)
    converted = list(
        map(
            lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
            lst
        )
    )

    return converted


minutes_list = create_minutes_list()

print(minutes_list)

#Task15

def write_sorted_list():

    minutes_list.sort(key=lambda x: x[1])

    converted = list(
        map(
            lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
            minutes_list
        )
    )

    try:
        with open("./minutes.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(minutes1["fields"])

            for row in converted:
                writer.writerow(row)

    except Exception as e:
        print("Error writing minutes.csv")
        print(e)
        exit()

    return converted

sorted_minutes_list = write_sorted_list()

print(sorted_minutes_list)
