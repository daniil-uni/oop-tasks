class Student:
def __init__(self, student_id, name):
self.student_id = student_id 
self.name = name 

class University:
def __init__(self, name):
self.name = name
self.students = [] 

def register_student(self, student):
self.students.append(student)
print(f"Студент {student.name} (ID: {student.student_id}) добавлен в университет {self.name}")

student1 = Student(1, "Артем")
uni1 = University("КазНУ")
uni2 = University("ЕНУ")

uni1.register_student(student1)
uni2.register_student(student1)