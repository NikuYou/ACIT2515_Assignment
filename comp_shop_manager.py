import datetime as date
from abstract_part import AbstractPart
import shop_stats
from cpu import Cpu
from gpu import Gpu


class ComputerShopManager:
    """Computer Shop Manager Class"""
    ID_DISPLAY = "ID"
    TYPE_DISPLAY = "Part Type"

    def __init__(self):
        """Initialize the Computer Shop Manager"""
        self._inventory = list()
        self._next_available_id = 1

    def add_part(self, part):
        """Add a part to the inventory list"""
        ComputerShopManager._validate_part_type(part)
        for existing_part in self._inventory:
            if part.get_model() == existing_part.get_model():
                raise ValueError("Part of the same model already exist.")
        part.ID = self._next_available_id
        self._inventory.append(part)
        self._next_available_id += 1

    def get_part_by_id(self, ID):
        """Get a part by ID"""
        ComputerShopManager._validate_int(ComputerShopManager.ID_DISPLAY, ID)
        int_id = int(ID)
        for parts in self._inventory:
            if parts.ID == int_id:
                return parts
        return None

    def get_all(self):
        """Get all parts"""
        return self._inventory

    def get_all_by_type(self, part_type):
        """Get all parts with the same type entered"""
        ComputerShopManager._validate_string(ComputerShopManager.TYPE_DISPLAY, part_type)
        part_type_list = list()
        for parts in self._inventory:
            if parts.get_part_type() == part_type:
                part_type_list.append(parts)
        return part_type_list

    def update(self, part):
        """Replace a part in the inventory based on ID"""
        ComputerShopManager._validate_part_type(part)
        for parts in self._inventory:
            if parts.ID == part.ID:
                self._inventory.remove(parts)
                self._inventory.append(part)
                return
        raise ValueError("Parts with the same ID does not exist in the inventory.")

    def delete_by_id(self, ID):
        """Delete a part by ID"""
        ComputerShopManager._validate_int(ComputerShopManager.ID_DISPLAY, ID)
        int_id = int(ID)
        for parts in self._inventory:
            if parts.ID == int_id:
                self._inventory.remove(parts)
                return
        raise ValueError("Parts with the same ID does not exist in the inventory.")

    def get_discontinued_stock_list(self):
        """Get list of all discontinued parts with stock"""
        discontinued_part_list = list()
        for parts in self._inventory:
            if (parts.is_discontinued() is True) and (parts.get_stock() > 0):
                discontinued_part_list.append(parts)
        return discontinued_part_list

    def get_shop_stats(self):
        """get the Inventory stats for the store"""
        total_parts_model = 0
        num_cpu_model = 0
        num_gpu_model = 0
        total_stock = 0
        num_cpu_stock = 0
        num_gpu_stock = 0
        discontinued_stock = 0

        for parts in self._inventory:
            total_parts_model += 1
            total_stock += parts.get_stock()
            if parts.get_part_type() == 'CPU':
                num_cpu_model += 1
                num_cpu_stock += parts.get_stock()
            elif parts.get_part_type() == 'GPU':
                num_gpu_model += 1
                num_gpu_stock += parts.get_stock()
            if parts.is_discontinued() is True:
                discontinued_stock += parts.get_stock()

        shop_stat_obj = shop_stats.ShopStats(total_parts_model, num_cpu_model, num_gpu_model,
                                             total_stock,
                                             num_cpu_stock, num_gpu_stock, discontinued_stock)
        return shop_stat_obj

    @staticmethod
    def _validate_string(display_name, str_input):
        if str_input is None:
            raise ValueError(display_name + ' cannot be undefined.')
        elif type(str_input) != str:
            raise ValueError(display_name + ' has to be a string.')
        elif str_input == "":
            raise ValueError(display_name + ' cannot be empty.')

    @staticmethod
    def _validate_part_type(part):
        if type(part) != Cpu and type(part) != Gpu:
            raise ValueError('The part you have added is not the right format')

    @staticmethod
    def _validate_int(display_name, int_input):
        if (isinstance(int_input, (float, int)) is False) or (int_input is None):
            raise ValueError(display_name + ' you have entered is invalid')
