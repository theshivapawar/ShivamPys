class Employee:
    id_counter = 0
    PF_PERCENT = 12
    PT = 200
    HRA_PERCENT = 50

    def __init__(self, name, basic, medical_allowance=0):
        Employee.id_counter += 1
        self.id = Employee.id_counter
        self.name = name
        self.basic = basic
        self.medical_allowance = medical_allowance

    def get_pf(self):
        return Employee.PF_PERCENT * self.basic

    def get_hra(self):
        return Employee.HRA_PERCENT * self.basic

    def calculate_gross(self):
        return self.basic + self.get_hra() + self.medical_allowance

    def calculate_net(self):
        return self.calculate_gross() - self.get_pf() - Employee.PT

    def __str__(self):
        return f'Employee > ID: {self.id} | Name: {self.name} | Gross: {self.calculate_gross()} | Net: {self.calculate_net()}'
