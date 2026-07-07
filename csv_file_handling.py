import csv
filename="employees.csv"
def employee_exists(emp_id):
    try:
        with open(filename,"r") as file:
            reader=csv.reader(file)
            for employee in reader:
                if employee[0]==emp_id:
                    return True
    except FileNotFoundError:
        return False
    return False
def add_employee():
    emp_id=input("Enter employee id:")
    if employee_exists(emp_id):
        print("Employee ID already exists!")
        return
    name=input("Enter employee name:")
    salary=input("Enter salary:")
    with open(filename,"a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([emp_id,name,salary])
    print("Employee added successfully")
def read_employees():
    try:
        with open(filename,"r") as file:
            reader=csv.reader(file)
            for employee in reader:
                print(employee)
    except FileNotFoundError:
        print("No employee records found")
def search_employees():
    emp_id=input("Enter employee ID to search:")
    try:
        with open(filename,"r") as file:
            reader=csv.reader(file)
            for employee in reader:
                if employee[0]==emp_id:
                    print("Employee found:",employee)
                    return
    except FileNotFoundError:
        print("Employee file not found")
        return
    print("Employee not found")
n=int(input("How many employees do you want to add?:"))
for i in range(n):
    print("\nEnter Employee",i+1)
    add_employee()
print("\nAll Employees:")
read_employees()
print("\nSearch Employee:")
search_employees()
