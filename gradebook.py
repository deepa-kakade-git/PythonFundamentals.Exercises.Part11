
from enum import Enum
from uuid import uuid4


class AliveStatus(Enum):
    Deceased = 0
    Alive = 1

class Person:
    def __init__(self, first_name, last_name, dob, alive):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = alive

    def update_first_name(self, new_first_name):
        self.first_name = new_first_name

    def update_last_name(self, new_last_name):
        self.last_name = new_last_name

    def update_dob(self, new_dob):
        self.dob = new_dob

    def update_status(self, new_status):
        self.alive = new_status

class Instructor(Person):
    def __init__(self, first_name, last_name, dob, alive, instructor_id):
        super().__init__(first_name, last_name, dob, alive)
        self.instructor_id = "Instructor_" + str(uuid4())

class Student(Person):
    def __init__(self, first_name, last_name, dob, alive, student_id):
        super().__init__(first_name, last_name, dob, alive)
        self.student_id = "Student_" + str(uuid4())

class ZipCodeStudent(Student):
    pass

class PrekStudent(Student):
    pass

class MiddleSchool(Student):
    pass

class CollegeStudent(Student):
    pass

class Classroom:
    def __init__(self):
        self.students = []
        self.instructors = []

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def remove_instructor(self, instructor):
        self.instructors.remove(instructor)

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def print_instructors(self):
        print("Instructors")
        for instructor in self.instructors:
            print(f"{instructor.first_name} {instructor.last_name}")

    def print_students(self):
        print("Students")
        for student in self.students:
            print(f"{student.first_name} {student.last_name}")


if __name__ == "__main__":
    instructor = Instructor("John", "Doe", "1980-01-01", AliveStatus.Alive, "Instructor_1")
    student1 = Student("Alice", "Smith", "1992-02-02", AliveStatus.Alive, "Student_1")
    student2 = Student("Tia", "Brooks", "1995-04-04", AliveStatus.Alive, "Student_2")

    classroom = Classroom()
    classroom.add_instructor(instructor)
    classroom.add_student(student1)
    classroom.add_student(student2)

    classroom.print_instructors()
    classroom.print_students()
