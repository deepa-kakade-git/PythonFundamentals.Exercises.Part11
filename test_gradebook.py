import unittest
from uuid import UUID

from gradebook import AliveStatus, Person, Instructor, Student, ZipCodeStudent, PrekStudent, MiddleSchool, CollegeStudent, Classroom


class TestPerson(unittest.TestCase):
    def test_update_first_name(self):
        person = Person("John", "Doe", "1980-01-01", AliveStatus.Alive)
        person.update_first_name("Jane")
        self.assertEqual(person.first_name, "Jane")

    def test_update_last_name(self):
        person = Person("John", "Doe", "1980-01-01", AliveStatus.Alive)
        person.update_last_name("Smith")
        self.assertEqual(person.last_name, "Smith")

    def test_update_dob(self):
        person = Person("John", "Doe", "1980-01-01", AliveStatus.Alive)
        person.update_dob("1990-02-02")
        self.assertEqual(person.dob, "1990-02-02")

    def test_update_status(self):
        person = Person("John", "Doe", "1980-01-01", AliveStatus.Alive)
        person.update_status(AliveStatus.Deceased)
        self.assertEqual(person.alive, AliveStatus.Deceased)


class TestInstructor(unittest.TestCase):
    def test_instructor_id_format(self):
        instructor = Instructor("John", "Doe", "1980-01-01", AliveStatus.Alive, "Instructor_1")
        self.assertTrue(instructor.instructor_id.startswith("Instructor_"))
        self.assertIsInstance(UUID(instructor.instructor_id.split("_")[1]), UUID)


class TestStudent(unittest.TestCase):
    def test_student_id_format(self):
        student = Student("Alice", "Smith", "1992-02-02", AliveStatus.Alive, "Student_1")
        self.assertTrue(student.student_id.startswith("Student_"))
        self.assertIsInstance(UUID(student.student_id.split("_")[1]), UUID)


class TestClassroom(unittest.TestCase):
    def setUp(self):
        self.classroom = Classroom()
        self.instructor = Instructor("John", "Doe", "1980-01-01", AliveStatus.Alive, "Instructor_1")
        self.student1 = Student("Alice", "Smith", "1992-02-02", AliveStatus.Alive, "Student_1")
        self.student2 = Student("Tia", "Brooks", "1995-04-04", AliveStatus.Alive, "Student_2")

    def test_add_instructor(self):
        self.classroom.add_instructor(self.instructor)
        self.assertIn(self.instructor, self.classroom.instructors)

    def test_remove_instructor(self):
        self.classroom.add_instructor(self.instructor)
        self.classroom.remove_instructor(self.instructor)
        self.assertNotIn(self.instructor, self.classroom.instructors)

    def test_add_student(self):
        self.classroom.add_student(self.student1)
        self.assertIn(self.student1, self.classroom.students)

    def test_remove_student(self):
        self.classroom.add_student(self.student1)
        self.classroom.remove_student(self.student1)
        self.assertNotIn(self.student1, self.classroom.students)


if __name__ == "__main__":
    unittest.main()