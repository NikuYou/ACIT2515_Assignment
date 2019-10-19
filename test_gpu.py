from unittest import TestCase
from gpu import Gpu
import unittest
import inspect

class TestGpu(TestCase):
    """unit test for Gpu class"""

    def setUp(self):
        """Create a test fixture before test method is run"""
        self.logGpu()
        self.gpu = Gpu(1920, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')
        self.assertIsNotNone(self.gpu)

    def tearDown(self):
        """ Destroys test data and calls logGpu"""
        self.logGpu()

    def logGpu(self):
        """test log"""
        currentTest = self.id().split('.')[-1]

        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_constructor_valid(self):
        """TG-010A: Tests for the successful creation of Gpu object"""
        self.assertIsNotNone(self.gpu)

    def test_constructor_invalid(self):
        """TG-010B: Tests for the failed creation of Gpu object"""
        self.assertRaisesRegex(ValueError, "Clock Speed you have entered is invalid", Gpu,None, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "Clock Speed you have entered is invalid", Gpu,"abc", 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "Clock Speed you have entered is invalid", Gpu,-1.0, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')

        self.assertRaisesRegex(ValueError, "Boost Clock you have entered is invalid", Gpu,1920, None, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "Boost Clock you have entered is invalid", Gpu,1920, "abc", "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "Boost Clock you have entered is invalid", Gpu,1920, -1.0, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')

        self.assertRaisesRegex(ValueError, "GPU Chipset cannot be undefined.", Gpu,1920, 2100, None, 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "GPU Chipset has to be a string.", Gpu,1920, 2100, self.gpu, 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "GPU Chipset cannot be empty.", Gpu,1920, 2100, "", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')

        self.assertRaisesRegex(ValueError, "PCIE version you have entered is invalid", Gpu,1920, 2100, "TU104A", None, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "PCIE version you have entered is invalid", Gpu,1920, 2100, "TU104A", "abc", 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "PCIE version you have entered is invalid", Gpu,1920, 2100, "TU104A", -0.1, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')

        self.assertRaisesRegex(ValueError, "GPU Length you have entered is invalid", Gpu,1920, 2100, "TU104A", 3.0, None, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "GPU Length you have entered is invalid", Gpu,1920, 2100, "TU104A", 3.0, "abc", 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "GPU Length you have entered is invalid", Gpu,1920, 2100, "TU104A", 3.0, -1.0, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')

        self.assertRaisesRegex(ValueError, "GPU Thickness you have entered is invalid", Gpu,1920, 2100, "TU104A", 3.0, 26.5, None, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "GPU Thickness you have entered is invalid", Gpu,1920, 2100, "TU104A", 3.0, 26.5, "abc", '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "GPU Thickness you have entered is invalid", Gpu,1920, 2100, "TU104A", 3.0, 26.5, -1.0, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')

        self.assertRaisesRegex(ValueError, "Model cannot be undefined.", Gpu,1920, 2100, "TU104A", 3.0, 26.5, 4.5, None, 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "Model has to be a string.", Gpu,1920, 2100, "TU104A", 3.0, 26.5, 4.5, self.gpu, 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "Model cannot be empty.", Gpu,1920, 2100, "TU104A", 3.0, 26.5, 4.5, "", 'Gigabyte', 1199.99, 980.20, 10, '2019-1-2')       

        self.assertRaisesRegex(ValueError, "Manufacturer cannot be undefined.", Gpu,1920, 2100, "TU104A", 3.0, 26.5, 4.5,'2080Ti Water Force', None, 1199.99, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "Manufacturer has to be a string.", Gpu,1920, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', self.gpu, 1199.99, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "Manufacturer cannot be empty.", Gpu,1920, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', "", 1199.99, 980.20, 10, '2019-1-2')     

        self.assertRaisesRegex(ValueError, "Price you have entered is invalid", Gpu,1920, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', None, 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "Price you have entered is invalid", Gpu,1920, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', "abc", 980.20, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "Price you have entered is invalid", Gpu,1920, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', -1.0, 980.20, 10, '2019-1-2')

        self.assertRaisesRegex(ValueError, "Cost you have entered is invalid", Gpu,1920, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, None, 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "Cost you have entered is invalid", Gpu,1920, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, "abc", 10, '2019-1-2')
        self.assertRaisesRegex(ValueError, "Cost you have entered is invalid", Gpu,1920, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, -1.0, 10, '2019-1-2')

        self.assertRaisesRegex(ValueError, "The stock value you have entered is invalid", Gpu,1920, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, None, '2019-1-2')
        self.assertRaisesRegex(ValueError, "The stock value you have entered is invalid", Gpu,1920, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, "abc", '2019-1-2')
        self.assertRaisesRegex(ValueError, "The stock value you have entered is invalid", Gpu,1920, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, -1, '2019-1-2')

        self.assertRaisesRegex(ValueError, "The release date cannot be empty.", Gpu,1920, 2100, "TU104A", 3.0, 26.5, 4.5, '2080Ti Water Force', 'Gigabyte', 1199.99, 980.20, 10, "")

    def test_get_clock_speed(self):
        """TG-020A: Tests if the get_clock_speed returns correct value"""
        self.assertEqual(self.gpu.get_clock_speed(),1920)

    def test_get_boost_clock(self):
        """TG-030A: Tests if the get_boost_clock returns correct value"""
        self.assertEqual(self.gpu.get_boost_clock(),2100)

    def test_get_chipset(self):
        """TG-040A: Tests if the get_chipset returns correct value"""
        self.assertEqual(self.gpu.get_chipset(),"TU104A")

    def test_get_length(self):
        """TG-050A: Tests if the get_length returns correct value"""
        self.assertEqual(self.gpu.get_length(),26.5)

    def test_get_thickness(self):
        """TG-060A: Tests if the get_thickness returns correct value"""
        self.assertEqual(self.gpu.get_thickness(),4.5)

    def test_get_description(self):
        """TG-070A: Tests if the get_description returns correct value"""        
        self.assertEqual(self.gpu.get_description(),"The GPU model:2080Ti Water Force by Gigabyte has a base clock of 1920.0Mhz and boost clock of 2100.0Mhz. It runs on PCIE3.0. It has length:26.5cm and thickness:4.5cm.  It is released on 2019-01-02 00:00:00 and it is not discontinued.")
      
    def test_get_part_type(self):
        """TG-080A: Tests if the get_part_type returns correct value"""        
        self.assertEqual(self.gpu.get_part_type(),"GPU")

if __name__ == "__main__":
    unittest.main()