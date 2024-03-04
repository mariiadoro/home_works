from human import Human
from student import Student
from group import Group, GroupToFullError

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
assert gr.find_student('Jobs') == st1

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!