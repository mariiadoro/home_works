from student import Student


class GroupToFullError(Exception):
    """Use it when try to add more than 10 students in the group"""
    pass


class Group:
    max_students = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) > self.max_students:
            raise GroupToFullError("Group is too full, sorry!")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n {all_students}'
