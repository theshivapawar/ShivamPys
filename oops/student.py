from functools import reduce
from typing import override

from oops.result import Result


class Student:
    id_counter = 0
    def __init__(self, name, marks):
        Student.id_counter += 1
        self.id = Student.id_counter
        self.name = name
        self.marks = marks

    @override
    def __str__(self):
        return f'Student > ID: {self.id} | Name: {self.name} | Marks: {self.marks}'

    def calculate_percent(self):
        total = 0
        for mark in self.marks.values():
            total += mark
        return (total / 500) * 100


satyam = Student('Satyam', {'Math': 50, 'Chemistry': 50, 'Physics': 50, 'English': 50, 'Bio': 50})
shivam = Student('Shivam', {'Math': 40, 'Chemistry': 40, 'Physics': 40, 'English': 40, 'Bio': 40})

result = Result([satyam, shivam])
print(result.find_min_percent())
print(result.find_max_percent())


students = [satyam, shivam]

max = reduce(lambda x, y : x.calculate_percent if x.calculate_percent() > y.calculate_percent() else y, students)
print(max)