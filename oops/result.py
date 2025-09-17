class Result:
    def __init__(self, students):
        self.students = students

    def find_max_percent(self):
        max_value = 0
        for student in self.students:
            if student.calculate_percent() > max_value:
                max_value = student.calculate_percent()

        return max_value

    def find_min_percent(self):
        min_value = float('inf')
        for student in self.students:
            if student.calculate_percent() < min_value:
                min_value = student.calculate_percent()

        return min_value



