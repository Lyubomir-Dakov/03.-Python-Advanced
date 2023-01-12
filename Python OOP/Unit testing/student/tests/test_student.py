from project.student import Student
from unittest import TestCase, main


class StudentTest(TestCase):
    def test_if_student_initialization_is_correct_empty_courses(self):
        student = Student('Gosho')
        self.assertEqual({}, student.courses)
        self.assertEqual('Gosho', student.name)

    def test_if_student_initialization_is_correct(self):
        student = Student('Gosho', {'math': ['da', 'ne', 'moje bi']})
        self.assertEqual({'math': ['da', 'ne', 'moje bi']}, student.courses)
        self.assertEqual('Gosho', student.name)

    def test_enroll_when_course_name_in_courses(self):
        student = Student('Gosho', {'math': []})
        self.assertEqual("Course already added. Notes have been updated.", student.enroll('math', ['da', 'ne', 'moje bi']))
        self.assertEqual(['da', 'ne', 'moje bi'], student.courses['math'])
        self.assertEqual({'math': ['da', 'ne', 'moje bi']}, student.courses)

    def test_enroll_add_course_notes_equal_to_Y(self):
        student = Student('Gosho')
        self.assertEqual("Course and course notes have been added.", student.enroll('math', ['da', 'ne'], 'Y'))
        self.assertEqual({'math': ['da', 'ne']}, student.courses)

    def test_enroll_add_course_notes_equal_to_empty_string(self):
        student = Student('Gosho')
        self.assertEqual("Course and course notes have been added.", student.enroll('math', ['da', 'ne'], ''))
        self.assertEqual({'math': ['da', 'ne']}, student.courses)

    def test_enroll_add_course_notes_equal_to_string(self):
        student = Student('Gosho')
        self.assertEqual("Course has been added.", student.enroll('math', ['da', 'ne'], 'xa'))
        self.assertEqual({'math': []}, student.courses)

    def test_enroll_just_add_course(self):
        student = Student('Gosho')
        self.assertEqual("Course has been added.", student.enroll('math', [], 'dali'))
        self.assertEqual({'math': []}, student.courses)

    def test_add_notes_if_course_name_in_courses(self):
        student = Student('Gosho', {'math': ['da', 'ne']})
        self.assertEqual("Notes have been updated", student.add_notes('math', 'dali'))
        self.assertEqual({'math': ['da', 'ne', 'dali']}, student.courses)

    def test_add_not4es_if_course_name_not_in_courses(self):
        student = Student('Gosho')
        with self.assertRaises(Exception) as ex:
            student.add_notes('math', 'dali')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_if_name_in_courses(self):
        student = Student('Gosho', {'math': ['da', 'ne']})
        self.assertEqual("Course has been removed", student.leave_course('math'))
        self.assertEqual({}, student.courses)

    def test_leave_course_if_course_doesnt_exists(self):
        student = Student('Gosho')
        with self.assertRaises(Exception) as ex:
            student.leave_course('math')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
