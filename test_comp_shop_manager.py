from unittest import TestCase
from comp_shop_manager import ComputerShopManager
from cpu import Cpu
from gpu import Gpu
from shop_stats import ShopStats
import unittest
import inspect

class TestManager(TestCase):
    """unit test for computer shop manager class"""

    def setUp(self):
        """Create a test fixture before test method is run"""
        self.logManager()
        self.manager = ComputerShopManager()
        self.cpu = Cpu(3.9, 4.6, 8, '1151v2', True, 'i9-9900k', 'Intel', 659.99, 580.50, 10, '2018-11-20')
        self.gpu = Gpu(1920, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')
        self.assertIsNotNone(self.manager)
        self.assertIsNotNone(self.cpu)
        self.assertIsNotNone(self.gpu)

    def tearDown(self):
        """ Destroys test data and calls logManager"""
        self.logManager()

    def logManager(self):
        """test log"""
        currentTest = self.id().split('.')[-1]

        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_constructor(self):
        """010A - Valid Construction"""
        self.assertIsNotNone(self.manager, "ComputerShopManager must be defined")

    def test_add_part_valid(self):
        """020A - Tests for successful add part"""
        self.manager.add_part(self.cpu)
        self.manager.add_part(self.gpu)
        self.assertEqual(2,len(self.manager.get_all()))

    def test_add_part_invalid(self):
        """020B - Tests for failed add part"""
        self.manager.add_part(self.cpu)
        self.manager.add_part(self.gpu)
        self.assertRaisesRegex(ValueError, "Part of the same model already exist.", self.manager.add_part,self.cpu)
        self.assertRaisesRegex(ValueError, "The part you have added is not the right format", self.manager.add_part,None)
        
    
    def test_get_part_by_id_valid(self):
        """030A - Tests for successful get part by id"""
        self.manager.add_part(self.cpu)
        self.manager.add_part(self.gpu)
        self.assertEqual(self.cpu,self.manager.get_part_by_id(1))

    def test_get_part_by_id_invalid(self):
        """030B - Tests for failed get part by id"""
        self.manager.add_part(self.cpu)
        self.manager.add_part(self.gpu)
        self.assertRaisesRegex(ValueError, "ID you have entered is invalid", self.manager.get_part_by_id,None)
        self.assertIsNone(self.manager.get_part_by_id(10))

    def test_get_all(self):
        """040A - Tests for get all parts"""
        self.manager.add_part(self.cpu)
        self.manager.add_part(self.gpu)
        self.assertEqual(2, len(self.manager.get_all()))
        self.assertEqual(self.cpu, self.manager.get_all()[0])
        self.assertEqual(self.gpu, self.manager.get_all()[1])

    def test_get_all_by_type_valid(self):
        """050A - Tests for successful get all parts by type"""
        self.manager.add_part(self.cpu)
        self.assertEqual([self.cpu],self.manager.get_all_by_type("CPU"))

    def test_get_all_by_type_invalid(self):
        """050B - Tests for failed get all parts by type"""
        self.assertRaisesRegex(ValueError,"Part Type cannot be undefined.",self.manager.get_all_by_type,None)
        self.assertRaisesRegex(ValueError,"Part Type cannot be empty.",self.manager.get_all_by_type,"")
        self.assertRaisesRegex(ValueError,"Part Type has to be a string.",self.manager.get_all_by_type,self.manager)

    def test_update_valid(self):
        """060A - Tests for successful replace a part in the inventory"""
        self.manager.add_part(self.cpu)
        self.manager.add_part(self.gpu)
        newcpu = Cpu(3.9, 4.5, 8, '1151v2', True, 'i9-9900', 'Intel', 629.99, 580.50, 10, '2018-11-20',1)
        self.manager.update(newcpu)
        self.assertEqual(newcpu,self.manager.get_part_by_id(1))


    def test_update_invalid(self):
        """060B - Tests for failed replace a part in the inventory"""
        self.assertRaisesRegex(ValueError,"Parts with the same ID does not exist in the inventory.",self.manager.update,self.cpu)
        self.assertRaisesRegex(ValueError,"The part you have added is not the right format",self.manager.update,None)

    def test_delete_by_id_valid(self):
        """070A - Tests for successful delete by id"""
        self.manager.add_part(self.cpu)
        self.manager.add_part(self.gpu)
        self.manager.delete_by_id(1)
        self.assertEqual(self.gpu,self.manager.get_all()[0])

    def test_delete_by_id_invalid(self):
        """070B - Tests for failed delete by id"""
        self.assertRaisesRegex(ValueError,"ID you have entered is invalid",self.manager.delete_by_id,"a")
        self.assertRaisesRegex(ValueError,"Parts with the same ID does not exist in the inventory.",self.manager.delete_by_id,3)

    def test_get_discontinued_stock_list(self):
        """080A - Tests for successful get discontinued stock list"""
        self.manager.add_part(self.cpu)
        self.manager.add_part(self.gpu)
        self.assertEqual(0, len(self.manager.get_discontinued_stock_list()))

    def test_get_shop_stats(self):
        """090A - Tests for successful get shop stats"""
        self.manager.add_part(self.cpu)
        self.manager.add_part(self.gpu)
        self.assertEqual(2,self.manager.get_shop_stats().get_total_parts_model())
        self.assertEqual(1,self.manager.get_shop_stats().get_num_cpu_model())
        self.assertEqual(1,self.manager.get_shop_stats().get_num_gpu_model())
        self.assertEqual(20,self.manager.get_shop_stats().get_total_stock())
        self.assertEqual(10,self.manager.get_shop_stats().get_num_cpu_stock())
        self.assertEqual(10,self.manager.get_shop_stats().get_num_gpu_stock())
        self.assertEqual(0,self.manager.get_shop_stats().get_discontinued_stock())
        

if __name__ == "__main__":
    unittest.main()