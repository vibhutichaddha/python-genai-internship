employees = [
    {"name":"A","salary":50000},
    {"name":"B","salary":70000},
    {"name":"C","salary":65000}
]
def salary_statistics(employees):
    salaries=[employee["salary"] for employee in employees]
    highest_salary=max(salaries)
    lowest_salary=min(salaries)
    average_salary=sum(salaries)/len(salaries)
    return highest_salary,lowest_salary,average_salary
print(salary_statistics(employees))