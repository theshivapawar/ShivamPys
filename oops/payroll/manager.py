from oops.employee import Employee


class Manager(Employee):
    def calculate_gross(self):
        return self.basic + self.get_hra() + self.medical_allowance + 

    def calculate_net(self):
        return self.calculate_gross() - self.get_pf() - Employee.PT