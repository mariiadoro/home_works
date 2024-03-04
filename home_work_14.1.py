class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, gender: {self.gender}, age: {self.age}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, record book: {self.record_book}"


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
        return f'Number:{self.number}\n {all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# For testing
# st3 = Student('Male', 30, 'Harry', 'Pother', 'AN145')
# st4 = Student('Female', 25, 'Ginny', 'Weasly', 'AN145')
# st5 = Student('Male', 30, 'Ron', 'Weasly', 'AN145')
# st6 = Student('Female', 25, 'Luna', 'Lovegood', 'AN145')
# st7 = Student('Male', 30, 'Severus', 'Snape', 'AN145')
# st8 = Student('Female', 25, 'Jennifer', 'Aniston', 'AN145')
# st9 = Student('Male', 30, 'Johny', 'Depp', 'AN145')
# st10 = Student('Female', 25, 'Hermione', 'Granger', 'AN145')
# st11 = Student('Male', 30, 'Draco', 'Malfoy', 'AN145')
gr = Group('PD1')
try:
    for _ in range(Group.max_students + 1):
        gr.add_student(st1)
        gr.add_student(st2)
        # For testing
        # gr.add_student(st3)
        # gr.add_student(st4)
        # gr.add_student(st5)
        # gr.add_student(st6)
        # gr.add_student(st7)
        # gr.add_student(st8)
        # gr.add_student(st9)
        # gr.add_student(st10)
        # gr.add_student(st11)
except GroupToFullError as e:
    print(e)
else:
    print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку має повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!