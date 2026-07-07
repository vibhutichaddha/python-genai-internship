import logging
import os
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/application.log",level=logging.INFO,format="%(asctime)s-%(levelname)s-%(message)s")
def add_employee():
    name=input("Enter employee name:")
    if not name:
        logging.warning("Invalid input while adding employee")
        print("Invalid input")
        return
    logging.info(f"Employee added:{name}")
    print("Employee added successfully")
def update_employee():
    emp_id=input("Enter employee ID to update:")
    logging.info(f"Employee updated:{emp_id}")
    print("Employee updated successfully")
def delete_employee():
    emp_id=input("Enter employee ID to be deleted:")
    logging.info(f"Employee deleted:{emp_id}")
    print("Employee deleted successfully")
try:
    add_employee()
    update_employee()
    delete_employee()
except Exception as error:
    logging.exception(f"Exception occured:{error}")
    print("An error occurred")