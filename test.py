from abstract_part import AbstractPart
from cpu import Cpu
from gpu import Gpu
from comp_shop_manager import ComputerShopManager
from unittest import TestCase
import time
import inspect


def main():
    bryanshop = ComputerShopManager()
    cpu1 = Cpu(3.9, 4.6, 8, '1151v2', True, 'i9-9900k', 'Intel', 659.99, 580.50, 10, '2018-11-20')
    cpu2 = Cpu(3.9, 4.5, 8, '1151v2', True, 'i9-9900', 'Intel', 629.99, 580.50, 10, '2018-11-20')
    gpu1 = Gpu(1920, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')

    bryanshop.add_part(cpu1)
    bryanshop.add_part(cpu2)
    bryanshop.add_part(gpu1)


if __name__ == "__main__":
    main()


class TestCpu(TestCase):
    """Unit test for Course"""

    def setUp(self):
        """ Sets up test data and calls logCourse"""
        self.logPoint()
        self.cpu = Cpu(3.9, 4.6, 8, '1151v2', True, 'i9-9900k', 'Intel', 659.99, 580.50, 10,
                          '2018-11-20', 1)
        self.assertIsNotNone(self.cpu)

    def tearDown(self):
        self.logPoint()
        """ Destroys test data and calls logCourse"""

    def logPoint(self):
        currentTest = self.id().split('.')[-1]

        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_cpu(self):
        """ 010A - Valid Construction """

        test_cpu = Cpu(3.9, 4.5, 8, '1151v2', True, 'i9-9900', 'Intel', 629.99, 580.50, 10, '2018-11-20')
        self.assertIsNotNone(test_cpu, "Course must be defined")

    def test_course_invalid_parameters(self):
        """ 010B - Invalid Construction Parameters """
        undefined_para = None
        empty_para = ""

        # Must reject an undefined parameter
        self.assertRaisesRegex(ValueError, "Course ID cannot be undefined.", Course,
                               undefined_para, "123456", "CIT")
        self.assertRaisesRegex(ValueError, "CRN cannot be undefined.", Course,
                               "ABCD1234", undefined_para, "CIT")
        self.assertRaisesRegex(ValueError, "Program cannot be undefined.", Course,
                               "ABCD1234", "123456", undefined_para)

        # Must reject an empty parameter
        self.assertRaisesRegex(ValueError, "Course ID cannot be empty.", Course,
                               empty_para, "123456", "CIT")
        self.assertRaisesRegex(ValueError, "CRN cannot be empty.", Course,
                               "ABCD1234", empty_para, "CIT")
        self.assertRaisesRegex(ValueError, "Program cannot be empty.", Course,
                               "ABCD1234", "123456", empty_para)

    def test_course_invalid_format(self):
        """ 010C - Invalid formatted Parameters """

        # Must reject an invalid formatted parameter
        self.assertRaisesRegex(ValueError, "Course ID has an incorrect format", Course,
                               "ABCDE", "123456", "CIT")
        self.assertRaisesRegex(ValueError, "CRN has an incorrect format", Course,
                               "ABCD1234", "123", "CIT")

    def test_get_course(self):
        """ 020A - test if get_course method returns correct value"""
        self.assertEqual(self.course.get_course_id(), "ABCD1234")

    def test_get_crn(self):
        """ 030A - test if get_course method returns correct value"""
        self.assertEqual(self.course.get_crn(), "123456")

    def test_get_program(self):
        """ 040A - test if get_course method returns correct value"""
        self.assertEqual(self.course.get_program(), "CIT")

    def test_add_student_valid(self):
        """ 050A - test add_student with valid input"""
        self.assertFalse(self.course.is_enrolled_in_course("A12345678"))
        self.course.add_student("A12345678")
        self.assertTrue(self.course.is_enrolled_in_course("A12345678"))

    def test_add_student_invalid_parameters(self):
        """ 050B - Invalid Construction Parameters """
        undefined_para = None
        empty_para = ""

        # Must reject an undefined parameter
        self.assertRaisesRegex(ValueError, "Student ID cannot be undefined.",
                               self.course.add_student, undefined_para)

        # Must reject an empty parameter
        self.assertRaisesRegex(ValueError, "Student ID cannot be empty.", self.course.add_student,
                               empty_para)

    def test_add_student_double(self):
        """ 050C - test add_student with existing Student"""
        self.course.add_student("A12345678")
        self.assertEqual(self.course.get_num_students(), 1)
        self.course.add_student("A12345678")
        self.assertEqual(self.course.get_num_students(), 1)

    def test_remove_student_valid(self):
        """ 060A - test remove_student with valid input"""
        self.course.add_student("A12345678")
        self.assertTrue(self.course.is_enrolled_in_course("A12345678"))
        self.course.remove_student("A12345678")
        self.assertFalse(self.course.is_enrolled_in_course("A12345678"))

    def test_remove_student_invalid_parameters(self):
        """ 060B - Invalid Construction Parameters """
        undefined_para = None
        empty_para = ""

        # Must reject an undefined parameter
        self.assertRaisesRegex(ValueError, "Student ID cannot be undefined.",
                               self.course.remove_student, undefined_para)

        # Must reject an empty parameter
        self.assertRaisesRegex(ValueError, "Student ID cannot be empty.",
                               self.course.remove_student,
                               empty_para)

    def test_remove_student_non_exist(self):
        """ 060C - test remove_student with existing Student"""
        self.course.add_student("B12345678")
        self.assertEqual(self.course.get_num_students(), 1)
        self.course.remove_student("A12345678")
        self.assertEqual(self.course.get_num_students(), 1)

    def test_is_enrolled_in_course_exist(self):
        """ 070A - test for existing student return True"""
        self.course.add_student("A12345678")
        self.assertTrue(self.course.is_enrolled_in_course("A12345678"))

    def test_is_enrolled_in_course_invalid(self):
        """ 070B - test for invalid parameter for is_enrolled_in_course method"""
        undefined_para = None
        empty_para = ""

        # Must reject an undefined parameter
        self.assertRaisesRegex(ValueError, "Student ID cannot be undefined.",
                               self.course.is_enrolled_in_course, undefined_para)

        # Must reject an empty parameter
        self.assertRaisesRegex(ValueError, "Student ID cannot be empty.",
                               self.course.is_enrolled_in_course,
                               empty_para)

    def test_is_enrolled_in_course_non_exist(self):
        """ 070C - test for non-existing student return False"""
        self.assertFalse(self.course.is_enrolled_in_course("A12345678"))

    def test_get_num_student_none_zero(self):
        """ 080A - test if get_num_student returns none 0"""
        self.course.add_student("A12345678")
        self.assertNotEqual(self.course.get_num_students(), 0)

    def test_get_num_student_zero(self):
        """ 080B - test if get_num_student returns 0"""
        self.assertEqual(self.course.get_num_students(), 0)

    def test_get_details_no_students(self):
        """ 090A - test if get_detail returns expected value no students"""
        expected_detail = "ABCD1234 (123456) is a course in the CIT Program with the following students: None"

        self.assertEqual(expected_detail, self.course.get_details())

    def test_get_details_with_students(self):
        """ 090B - test if get_detail returns expected value with students"""
        self.course.add_student("A12345678")
        expected_detail = "ABCD1234 (123456) is a course in the CIT Program with the following students: A12345678"

        self.assertEqual(expected_detail, self.course.get_details())