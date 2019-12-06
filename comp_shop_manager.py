from abstract_part import AbstractPart
import shop_stats
import os
import json
from cpu import Cpu
from gpu import Gpu
import re
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ComputerShopManager:
    """Computer Shop Manager Class"""

    def __init__(self, db_filename):
        """Initialize the Computer Shop Manager"""
        ComputerShopManager._validate_string("DB NAME", db_filename)

        engine = create_engine("sqlite:///" + db_filename)
        self._db_session = sessionmaker(bind=engine)

    def add_part(self, part):
        """Add a part to the inventory list"""
        ComputerShopManager._validate_part_type(part)

        session = self._db_session()
        part_exist = session.query(AbstractPart).filter(AbstractPart.model == part.model).first()
        if part_exist is not None:
            session.close()
            raise ValueError("Part of the same model already exist.")
        session.close()

        part_list = self.get_all()
        parts_id = []
        if len(part_list) > 0:
            for i in part_list:
                parts_id.append(i.id)
            part.id = max(parts_id)+1
        else:
            part.id = 1

        session = self._db_session()

        session.add(part)
        session.commit()

        session.close()

    def get_part_by_model(self, model):
        """Get a part by ID"""
        ComputerShopManager._validate_string("MODEL", model)
        session = self._db_session()
        part = session.query(Cpu).filter(Cpu.type == Cpu.PART_TYPE, Cpu.model == model).first()
        if part is None:
            part = session.query(Gpu).filter(Gpu.type == Gpu.PART_TYPE, Gpu.model == model).first()
        if part is None:
            session.close()
            raise ValueError("Parts with the same Model does not exist in the inventory.")
        session.close()
        return part

    def get_all(self):
        """Get all parts"""
        session = self._db_session()
        cpus = session.query(Cpu).filter(Cpu.type == Cpu.PART_TYPE).all()
        gpus = session.query(Gpu).filter(Gpu.type == Gpu.PART_TYPE).all()
        parts = []
        session.close()
        for i in cpus:
            parts.append(i)
        for i in gpus:
            parts.append(i)
        return parts

    def get_all_by_type(self, part_type):
        """Get all parts with the same type entered"""
        ComputerShopManager._validate_string("Part Type", part_type)
        if part_type != 'CPU' and part_type != 'GPU':
            raise ValueError('This type of part is not supported')

        session = self._db_session()

        if part_type == Cpu.PART_TYPE:
            parts = session.query(Cpu).filter(Cpu.type == 'CPU').all()
        elif part_type == Gpu.PART_TYPE:
            parts = session.query(Gpu).filter(Gpu.type == 'GPU').all()
        else:
            parts = []

        session.close()

        return parts

    def update(self, part):
        """update stock number and discontinued status in the inventory based on model"""
        session = self._db_session()
        old_part = session.query(AbstractPart).filter(AbstractPart.model == part['model']).first()

        if old_part is None:
            session.close()
            raise ValueError("Parts with the same Model does not exist in the inventory.")
        else:
            old_part.stock = part['stock']
            if part['is_discontinued'] == 1:
                old_part.is_discontinued = True
            else:
                old_part.is_discontinued = False
            session.commit()
            session.close()

    def delete_by_model(self, model):
        """Delete a part by ID"""
        ComputerShopManager._validate_string("MODEL", model)

        session = self._db_session()
        part = session.query(AbstractPart).filter(AbstractPart.model == model).first()

        if part is None:
            session.close()
            raise ValueError("Parts with the same Model does not exist in the inventory.")

        session.delete(part)
        session.commit()
        session.close()

    def get_discontinued_stock_list(self):
        """Get list of all discontinued parts with stock"""
        discontinued_part_list = list()

        session = self._db_session()

        all_parts = session.query(AbstractPart).all()

        session.close()

        for parts in all_parts:
            if (parts.is_discontinued == AbstractPart.BOOLEAN_TRUE) and (parts.stock > 0):
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

        session = self._db_session()

        all_parts = session.query(AbstractPart).all()

        session.close()

        for parts in all_parts:
            total_parts_model += 1
            total_stock += parts.stock
            if parts.type == 'CPU':
                num_cpu_model += 1
                num_cpu_stock += parts.stock
            elif parts.type == 'GPU':
                num_gpu_model += 1
                num_gpu_stock += parts.stock
            if parts.is_discontinued == AbstractPart.BOOLEAN_TRUE:
                discontinued_stock += parts.stock

        shop_stat_obj = shop_stats.ShopStats(total_parts_model, num_cpu_model, num_gpu_model, total_stock,
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
        elif display_name == "DB NAME":
            if re.match("^(.*/)?(?:$|(.+?)(?:(\.[^.]*$)|$))", str_input) is False:
                raise ValueError(display_name + ' cannot have invalid character.')

    @staticmethod
    def _validate_part_type(part):
        if type(part) != Cpu and type(part) != Gpu:
            raise ValueError('The part you have added is not the right format')

    @staticmethod
    def _validate_int(display_name, int_input):
        if (isinstance(int_input, (float, int)) is False) or (int_input is None):
            raise ValueError(display_name + ' you have entered is invalid')

