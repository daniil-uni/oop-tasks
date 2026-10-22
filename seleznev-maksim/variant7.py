class Course:
    def __init__(self,name, duration):
        self.name = name
        self.duration = duration

class LearningPlatform:
   def __init__(self,name):
       self.name = name
       self.courses = []

   def add_course(self, course):
       self.courses.append(course)

   def show_courses(self):
       print("Платформа:", self.name)
       for course in self.courses:
           print(course.name, "-", course.duration, "часов")

course1 = Course("Python", 20)
course2 = Course("Java", 30)

platform1 = LearningPlatform("Coursera")
platform2 = LearningPlatform("IT-step")

platform1.add_course(course1)
platform1.add_course(course2)
platform2.add_course(course1)

platform1.show_courses()
platform2.show_courses()