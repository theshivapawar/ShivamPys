class Employee:
    __id_counter = 0
    counter = 0
    def __init__(self, eid, name, salary):
        Employee.__id_counter += 1
        self.eid = Employee.__id_counter
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'str ID: {self.eid} | Name: {self.name} | Salary: {self.salary}'

    def __repr__(self):
        return f'repr ID: {self.eid} | Name: {self.name} | Salary: {self.salary}'

    # def __lt__(self, other):
    #     return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name

    @staticmethod
    def get_number_of_employees():
        return Employee.__id_counter

shivam = Employee(101, 'Shivam', 50000)
satyam = Employee(102, 'Satyam', 40000)


class Manager(Employee):
    pass

umang = Manager(103, 'Umang', 60000)

print(shivam.get_number_of_employees())
print(Employee._Employee__id_counter) #mangling