import json
filename="employees.json"
def load_employees():
    try:
        with open(filename,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
def save_employees(employees):
    with open(filename,"w") as file:
        json.dump(employees, file, indent=4)
def add_employees():
        employees=load_employees()
        emp_id=input("Enter employee id:")
        for employee in employees:
            if employee["id"]==emp_id:
                print("Employee ID already exists")
                return
        name=input("Enter employee name:")
        salary=float(input("Enter employee salary:"))
        employee={"id":emp_id,"name":name,"salary":salary}
        employees.append(employee)
        save_employees(employees)
        print("Employee added successfully!")
def read_employees():
    employees=load_employees()
    if not employees:
        print("No employees found")
        return
    for employee in employees:
        print(employee)
def update_salary():
    employees=load_employees()
    emp_id=input("Enter employee id:")
    for employee in employees:
        if employee["id"]==emp_id:
            new_salary=float(input("Enter new salary:"))
            employee["salary"]=new_salary
            save_employees(employees)
            print("Salary updated successfully")
            return
    print("Employee not found")
def delete_employee():
    employees=load_employees()
    emp_id=input("Enter employee ID:")
    for employee in employees:
        if employee["id"]==emp_id:
            employees.remove(employee)
            save_employees(employees)
            print("Employee deleted successfully")
            return
    print("Employee not found")
add_employees()
print("\nAll Employees:")
read_employees()
update_salary()
print("\nAfter update:")
read_employees()
delete_employee()
print("\nAfter Delete:")
read_employees()