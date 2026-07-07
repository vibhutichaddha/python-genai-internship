class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def calculate_bonus(self):
        return 0
class Developer(Employee):
    def calculate_bonus(self):
        return self.salary*0.10
class Manager(Employee):
    def calculate_bonus(self):
        return self.salary*0.20
developer = Developer(1,"Alice",50000)
manager = Manager(2,"Bob",80000)
print(f"Developer Bonus: {developer.calculate_bonus()}")
print(f"Manager Bonus: {manager.calculate_bonus()}")