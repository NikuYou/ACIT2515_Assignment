from unittest import TestCase
from cpu import Cpu
import unittest
import inspect


class TestCpu(TestCase):
    """unit test for Cpu class"""

    def setUp(self):
        """Create a test fixture before test method is run"""
        self.logCpu()
        self.cpu = Cpu(3.9, 4.6, 8, '1151v2', True, 'i9-9900k', 'Intel', 659.99, 580.50, 10, '2018-11-20')
        self.assertIsNotNone(self.cpu)

    def tearDown(self):
        """ Destroys test data and calls logCpu"""
        self.logCpu()

    def logCpu(self):
        currentTest = self.id().split('.')[-1]

        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_constructor_valid(self):
        test_cpu = Cpu(3.9, 4.6, 8, '1151v2', True, 'i9-9900', 'Intel', 659.99, 580.50, 10, '2018-11-20')
        """TC-010A: Tests for the successful creation of Cpu object"""
        self.assertIsNotNone(test_cpu)

    def test_constructor_invalid(self):
        """TC-010B: Tests for the failed creation of Gpu object"""
        self.assertRaisesRegex(ValueError, "Clock Speed you have entered is invalid",
                               Cpu, None, 4.6, 8, '1151v2', True, 'i9-9900', 'Intel', 659.99, 580.50, 10, '2018-11-20')
        self.assertRaisesRegex(ValueError, "Clock Speed you have entered is invalid",
                               Cpu, -1, 4.6, 8, '1151v2', True, 'i9-9900', 'Intel', 659.99, 580.50, 10, '2018-11-20')
        self.assertRaisesRegex(ValueError, "Clock Speed you have entered is invalid",
                               Cpu, '123', 4.6, 8, '1151v2', True, 'i9-9900', 'Intel', 659.99, 580.50, 10, '2018-11-20')

        self.assertRaisesRegex(ValueError, "Boost Clock you have entered is invalid",
                               Cpu, 3.9, None, 8, '1151v2', True, 'i9-9900', 'Intel', 659.99, 580.50, 10, '2018-11-20')
        self.assertRaisesRegex(ValueError, "Boost Clock you have entered is invalid",
                               Cpu, 3.9, -1, 8, '1151v2', True, 'i9-9900', 'Intel', 659.99, 580.50, 10, '2018-11-20')
        self.assertRaisesRegex(ValueError, "Boost Clock you have entered is invalid",
                               Cpu, 3.9, '123', 8, '1151v2', True, 'i9-9900', 'Intel', 659.99, 580.50, 10, '2018-11-20')

        self.assertRaisesRegex(ValueError, "Number of CPU cores you have entered is invalid",
                               Cpu, 3.9, 4.6, None, '1151v2', True, 'i9-9900k', 'Intel', 659.99, 580.50, 10,
                               '2018-11-20')
        self.assertRaisesRegex(ValueError, "Number of CPU cores you have entered is invalid",
                               Cpu, 3.9, 4.6, -10, '1151v2', True, 'i9-9900k', 'Intel', 659.99, 580.50, 10,
                               '2018-11-20')
        self.assertRaisesRegex(ValueError, "Number of CPU cores you have entered is invalid",
                               Cpu, 3.9, 4.6, "123", '1151v2', True, 'i9-9900k', 'Intel', 659.99, 580.50, 10,
                               '2018-11-20')

        self.assertRaisesRegex(ValueError, "Socket model cannot be empty.",
                               Cpu, 3.9, 4.6, 8, '', True, 'i9-9900k', 'Intel', 659.99, 580.50, 10, '2018-11-20')
        self.assertRaisesRegex(ValueError, "Socket model cannot be undefined.",
                               Cpu, 3.9, 4.6, 8, None, True, 'i9-9900k', 'Intel', 659.99, 580.50, 10, '2018-11-20')

        self.assertRaisesRegex(ValueError, "Hyper-threading Available Status you have entered is invalid",
                               Cpu, 3.9, 4.6, 8, '1151v2', None, 'i9-9900k', 'Intel', 659.99, 580.50, 10, '2018-11-20')

        self.assertRaisesRegex(ValueError, "Model cannot be empty.",
                               Cpu, 3.9, 4.6, 8, '1151v2', True, '', 'Intel', 659.99, 580.50, 10, '2018-11-20')
        self.assertRaisesRegex(ValueError, "Model cannot be undefined.",
                               Cpu, 3.9, 4.6, 8, '1151v2', True, None, 'Intel', 659.99, 580.50, 10, '2018-11-20')

        self.assertRaisesRegex(ValueError, "Manufacturer cannot be empty.",
                               Cpu, 3.9, 4.6, 8, '1151v2', True, 'i9-9900k', '', 659.99, 580.50, 10, '2018-11-20')
        self.assertRaisesRegex(ValueError, "Manufacturer cannot be undefined.",
                               Cpu, 3.9, 4.6, 8, '1151v2', True, 'i9-9900k', None, 659.99, 580.50, 10, '2018-11-20')

        self.assertRaisesRegex(ValueError, "Price you have entered is invalid",
                               Cpu, 3.9, 4.6, 8, '1151v2', True, 'i9-9900k', 'Intel', None, 580.50, 10, '2018-11-20')
        self.assertRaisesRegex(ValueError, "Price you have entered is invalid",
                               Cpu, 3.9, 4.6, 8, '1151v2', True, 'i9-9900k', 'Intel', '123', 580.50, 10, '2018-11-20')

        self.assertRaisesRegex(ValueError, "Cost you have entered is invalid",
                               Cpu, 3.9, 4.6, 8, '1151v2', True, 'i9-9900k', 'Intel', 659.99, None, 10, '2018-11-20')
        self.assertRaisesRegex(ValueError, "Cost you have entered is invalid",
                               Cpu, 3.9, 4.6, 8, '1151v2', True, 'i9-9900k', 'Intel', 659.99, '123', 10, '2018-11-20')

        self.assertRaisesRegex(ValueError, "The stock value you have entered is invalid",
                               Cpu, 3.9, 4.6, 8, '1151v2', True, 'i9-9900', 'Intel', 659.99, 580.50, None, '2018-11-20')
        self.assertRaisesRegex(ValueError, "The stock value you have entered is invalid",
                               Cpu, 3.9, 4.6, 8, '1151v2', True, 'i9-9900', 'Intel', 659.99, 580.50, -10, '2018-11-20')

        self.assertRaisesRegex(ValueError, "The release date cannot be empty or undefined.",
                               Cpu, 3.9, 4.6, 8, '1151v2', True, 'i9-9900', 'Intel', 659.99, 580.50, 10, None)
        self.assertRaisesRegex(ValueError, "The release date cannot be empty or undefined.",
                               Cpu, 3.9, 4.6, 8, '1151v2', True, 'i9-9900', 'Intel', 659.99, 580.50, 10, '')

        self.assertRaisesRegex(ValueError, "ID you have entered is invalid",
                               Cpu, 3.9, 4.6, 8, '1151v2', True, 'i9-9900', 'Intel', 659.99, 580.50, 10, '2018-11-20',
                               '123')
        self.assertRaisesRegex(ValueError, "ID you have entered is invalid",
                               Cpu, 3.9, 4.6, 8, '1151v2', True, 'i9-9900', 'Intel', 659.99, 580.50, 10, '2018-11-20',
                               None)

    def test_get_clock_speed(self):
        """TC-020A: Tests if the get_clock_speed returns correct value"""
        self.assertEqual(self.cpu.get_clock_speed(), 3.9)

    def test_get_boost_clock(self):
        """TC-030A: Tests if the get_boost_clock returns correct value"""
        self.assertEqual(self.cpu.get_boost_clock(), 4.6)

    def test_get_core_count(self):
        """TC-040A: Tests if the get_core_count returns correct value"""
        self.assertEqual(self.cpu.get_core_count(), 8)

    def test_get_hyperthread(self):
        """TC-050A: Tests if the get_hyperthread returns correct value"""
        self.assertEqual(self.cpu.get_hyperthread(), True)

    def test_get_description(self):
        """TC-060A: Tests if the get_description returns correct value"""
        self.assertEqual(self.cpu.get_description(),
                         "The CPU model:i9-9900k by Intel has 8 cores with hyperthreading. It has a base clock of 3.9Ghz and boost clock of 4.6Ghz, compatible with the socket 1151v2. It is released on 2018-11-20 00:00:00 and it is not discontinued.")

    def test_get_part_type(self):
        """TC-070A: Tests if the get_part_type returns correct value"""
        self.assertEqual(self.cpu.get_part_type(), "CPU")


if __name__ == "__main__":
    unittest.main()
