# Here we will try to find if a student can enroll to a course.
# So, we create two classes Student and Course and connect them.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # grade is from 0 to 100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []          # I can add this 'student' attribute in parameters of init function but it is also fine like this.
                                    # I create an empty list.

        # Now I create a method here which will add 'Student' object into the empty list.

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True # returns True if student is added.
        return False    # returns False if student is not added.

    def get_average_age(self):
        pass
       
        # I now create 3 'Student' objects as s1,s2 and s3
s1 = Student("Shree", 30, 90)
s2 = Student("Rojna", 27, 95)
s3 = Student("Roshi", 19, 98)

       # I create one Course object named course1 
course1 = Course("Physics", 3)

        # Now lets add these 'Student' objects to the Course class.

course1.add_student(s1) # 'course1' is an object of class 'Course' where 'add_student' is method
course1.add_student(s2)


print(course1.add_student(s1))
print(course1.add_student(s3))



