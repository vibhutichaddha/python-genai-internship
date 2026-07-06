class EmployeeNotFoundError(Exception):
    pass
class DuplicateEmployeeError(Exception):
    pass
class InvalidSalaryError(Exception):
    pass
employees=[]
def add_employees():
    try:
        emp_id=input("Enter Employee ID:")
        for emp in employees:
            if emp["id"]==emp_id:
                raise DuplicateEmployeeError("Employee ID already exists")
        name=input("Enter employee name:")
        salary=float(input("Enter employee salary"))
        if salary<=0:
            raise InvalidSalaryError("Salary must be greater than 0")
        emp={"id":emp_id,"name":name,"salary":salary}
        employees.append(emp)
        print("Employee added successfully")
    except DuplicateEmployeeError as error:
        print(error)
    except InvalidSalaryError as error:
        print(error)
    except ValueError:
        print("Invalid Input")
def search_employee():
    try:
        emp_id=input("Enter employee ID to search:")
        for emp in employees:
            if emp["id"]==emp_id:
                print("Employee Found:",emp) 
                return
            raise EmployeeNotFoundError("Employee not found")
    except EmployeeNotFoundError as error:
        print(error)
add_employees()
search_employee()