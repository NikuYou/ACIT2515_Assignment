from abstract_part import AbstractPart
from sqlalchemy import Column, String, Integer, Float, DateTime


class Gpu(AbstractPart):
    """Gpu Class"""
    PART_TYPE = "GPU"
    MIN_CLOCK_PCIE_LENGTH_THICKNESS = 0.0
    CLOCK_DISPLAY = "Clock Speed"
    BOOST_DISPLAY = "Boost Clock"
    CHIPSET_DISPLAY = "GPU Chipset"
    PCIE_VER__DISPLAY = "PCIE version"
    LENGTH_DISPLAY = "GPU Length"
    THICKNESS_DISPLAY = "GPU Thickness"

    clock_speed_mhz = Column(Float)
    boost_clock_mhz = Column(Float)
    pcie_ver = Column(Float)
    chipset = Column(String(20))
    length_cm = Column(Float)
    thickness_cm = Column(Float)

    def __init__(self, clock_speed_mhz, boost_clock_mhz, chipset, pcie_ver, length_cm, thickness_cm, model, manufacturer, sale_price, cost, stock, release_date_input, is_discontinued=False):
        """Initialize Gpu"""

        Gpu.validate_pos_float(Gpu.CLOCK_DISPLAY, clock_speed_mhz)
        Gpu.validate_pos_float(Gpu.BOOST_DISPLAY, boost_clock_mhz)
        Gpu.validate_string(Gpu.CHIPSET_DISPLAY, chipset)
        Gpu.validate_pos_float(Gpu.PCIE_VER__DISPLAY, pcie_ver)
        Gpu.validate_pos_float(Gpu.LENGTH_DISPLAY, length_cm)
        Gpu.validate_pos_float(Gpu.THICKNESS_DISPLAY, thickness_cm)

        self.clock_speed_mhz = float("%.2f" % clock_speed_mhz)
        self.boost_clock_mhz = float("%.2f" % boost_clock_mhz)
        self.chipset = chipset
        self.pcie_ver = float("%.1f" % pcie_ver)
        self.length_cm = float("%.2f" % length_cm)
        self.thickness_cm = float("%.2f" % thickness_cm)

        super().__init__(model, manufacturer, sale_price, cost, stock, release_date_input, Gpu.PART_TYPE, is_discontinued)

    def get_description(self):
        """get Part description"""
        if self.is_discontinued is True:
            discontinued_description = 'is discontinued'
        else:
            discontinued_description = 'is not discontinued'
        description = 'The GPU model:{} by {} has a base clock of {}Mhz and boost clock of {}Mhz. It runs on PCIE{}. It has length:{}cm and thickness:{}cm.  It is released on {} and it {}.'.format(
            self.model, self.manufacturer, self.clock_speed_mhz,
            self.boost_clock_mhz, self.pcie_ver, self.length_cm, self.thickness_cm, self.release_date,
            discontinued_description)
        return description

    def get_part_type(self):
        """Get Part type"""
        return Gpu.PART_TYPE

    def to_dict(self):
        """ Return dictionary of the part"""
        dict = {}
        dict['clock_speed_mhz'] = self.clock_speed_mhz
        dict['boost_clock_mhz'] = self.boost_clock_mhz
        dict['chipset'] = self.chipset
        dict['pcie_ver'] = self.pcie_ver
        dict['length_cm'] = self.length_cm
        dict['thickness_cm'] = self.thickness_cm
        dict['model'] = self.model
        dict['manufacturer'] = self.manufacturer
        dict['sale_price'] = self.sale_price
        dict['cost'] = self.cost
        dict['stock'] = self.stock
        dict['release_date'] = str(self.release_date.strftime("%Y-%m-%d"))
        dict['type'] = self.type
        dict['id'] = self.id
        dict['is_discontinued'] = self.is_discontinued
        return dict

    @staticmethod
    def validate_string(display_name, str_input):
        if str_input is None:
            raise ValueError(display_name + ' cannot be undefined.')
        elif type(str_input) != str:
            raise ValueError(display_name + ' has to be a string.')
        elif str_input == "":
            raise ValueError(display_name + ' cannot be empty.')

    @staticmethod
    def validate_pos_float(display_name, clock):
        """Validate the value of the clock speed variable """
        if (clock is None) or (isinstance(clock, (float, int)) is False) or (clock < Gpu.MIN_CLOCK_PCIE_LENGTH_THICKNESS):
            raise ValueError(display_name + ' you have entered is invalid')


