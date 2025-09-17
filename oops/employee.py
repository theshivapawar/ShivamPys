from typing import override


class Employee:
    def __init__(self, eid=0, name='', salary=0):
        self.eid= eid
        self.name = name
        self.salary = salary

    @override
    def __str__(self):
        return f'Employee > ID: {self.eid} | Name: {self.name} | Salary: {self.salary}'

class Developer(Employee):
    def __init__(self, eid, name, salary):
        super().__init__(eid, name, salary)



shivam = Developer(101, 'Shivam', 20000)
print(shivam)