from unittest import TestCase
from cpu import Cpu
import unittest
import inspect
from datetime import datetime

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

    def test_to_dict(self):
        """TC-080A Tests the to_dict() method """
        test_cpu = {
            "clock_speed_ghz": 3.9,
            "boost_clock_ghz": 4.6,
            "core_count": 8,
            "socket": '1151v2',
            "hyperthread": True,
            "model": 'i9-9900k',
            "manufacturer": 'Intel',
            "price": 659.99,
            "cost": 580.50,
            "stock": 10,
            "release_date": '2018-11-20',
            "type": "CPU",
            'id': 0,
            'is_discontinued': False
        }
        self.assertEqual(self.cpu.to_dict(), test_cpu)

    def test_is_discontinued(self):
        """TC-090A test get the boolean status of if the part is discontinued"""
        self.assertEqual(self.cpu.is_discontinued(), False)

    def test_get_cost(self):
        """TC-100A Test get cost method"""
        self.assertEqual(self.cpu.get_cost(), 580.50)

    def test_calc_profit(self):
        """TC-110A Test calc profit"""
        self.assertEqual(self.cpu.calc_profit(), 79.49)

    def test_set_price_valid(self):
        """TC-120A Test set price with valid input"""
        self.cpu.price = 680.50
        self.assertEqual(self.cpu.price, 680.50)

    def test_set_price_invalid(self):
        """TC-120A Test set price with invalid input"""
        self.assertRaisesRegex(ValueError, "Price you have entered is invalid", self.cpu._set_price, '123')

    def test_get_price(self):
        """TC-130A Test get price"""
        self.assertEqual(self.cpu.price, 659.99)

    def test_set_id_valid(self):
        """TC-140A Test set id with valid input"""
        self.cpu.id = 8
        self.assertEqual(self.cpu.id, 8)

    def test_set_id_invalid(self):
        """TC-140B Test set id with invalid input"""
        self.assertRaisesRegex(ValueError, "ID you have entered is invalid", self.cpu._set_id, '123')

    def test_get_id(self):
        """TC-150A Test get id"""
        self.assertEqual(self.cpu.id, 0)

    def test_get_model(self):
        """TC-160A Test get model"""
        self.assertEqual(self.cpu.get_model(), 'i9-9900k')

    def test_get_release_date(self):
        """TC-170A Test get release date"""
        test_release_date = datetime.strptime("2018-11-20", '%Y-%m-%d')
        self.assertEqual(self.cpu.get_release_date(), test_release_date)

    def test_get_stock(self):
        """TC-180A Test get stock"""
        self.assertEqual(self.cpu.get_stock(), 10)

    def test_add_stock_valid(self):
        """TG-190A Test add stock with valid input"""
        self.cpu.add_stock(20)
        self.assertEqual(self.cpu.get_stock(), 30)

    def test_add_stock_invalid(self):
        """TC-190B Test add stock with invalid input"""
        self.assertRaisesRegex(ValueError, "The stock value you have entered is invalid", self.cpu.add_stock, '123')

    def test_set_is_discontinued_valid(self):
        """TC-200A Test set discontinued with valid input"""
        self.cpu.set_is_discontinued(True)
        self.assertEqual(self.cpu.is_discontinued(), True)

    def test_set_is_discontinued_invalid(self):
        """TC-200B Test set discontinued with invalid input"""
        self.cpu.set_is_discontinued(True)
        self.assertRaisesRegex(ValueError, "Discontinued Status you have entered is invalid", self.cpu.set_is_discontinued, '123')


if __name__ == "__main__":
    unittest.main()
