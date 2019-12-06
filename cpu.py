from abstract_part import AbstractPart
from sqlalchemy import Column, String, Integer, Float, DateTime


class Cpu(AbstractPart):
    """Cpu Class"""
    PART_TYPE = "CPU"
    MIN_CLOCK = 0.0
    MIN_CORE = 0
    CLOCK_DISPLAY = "Clock Speed"
    BOOST_DISPLAY = "Boost Clock"
    CORE_COUNT_DISPLAY = "Number of CPU cores"
    SOCKET_DISPLAY = "Socket model"
    HYPERTHREAD_DISPLAY = "Hyper-threading Available Status"

    clock_speed_ghz = Column(Float)
    boost_clock_ghz = Column(Float)
    core_count = Column(Integer)
    socket = Column(String(20))
    hyperthread = Column(Integer)

    def __init__(self, clock_speed_ghz, boost_clock_ghz, core_count, socket, hyperthread, model, manufacturer, sale_price,
                 cost, stock, release_date_input, is_discontinued=False):
        """Initialize Cpu"""

        Cpu.validate_clock(Cpu.CLOCK_DISPLAY, clock_speed_ghz)
        Cpu.validate_clock(Cpu.BOOST_DISPLAY, boost_clock_ghz)
        Cpu.validate_core(Cpu.CORE_COUNT_DISPLAY, core_count)
        Cpu.validate_string(Cpu.SOCKET_DISPLAY, socket)
        Cpu.validate_bool(Cpu.HYPERTHREAD_DISPLAY, hyperthread)

        self.clock_speed_ghz = float("%.2f" % clock_speed_ghz)
        self.boost_clock_ghz = float("%.2f" % boost_clock_ghz)
        self.core_count = core_count
        self.socket = socket
        self.hyperthread = hyperthread

        super().__init__(model, manufacturer, sale_price, cost, stock, release_date_input, Cpu.PART_TYPE, is_discontinued)

    def get_hyperthread(self):
        """Get the Hyperthreading availability status (Boolean)"""
        if self.hyperthread == AbstractPart.BOOLEAN_TRUE:
            return True
        return False

    def get_description(self):
        """get Part description"""
        if self.hyperthread == AbstractPart.BOOLEAN_TRUE:
            hyperthread_description = 'with hyperthreading'
        else:
            hyperthread_description = 'with no hyperthreading'
        if self.is_discontinued == AbstractPart.BOOLEAN_TRUE:
            discontinued_description = 'is discontinued'
        else:
            discontinued_description = 'is not discontinued'
        description = 'The CPU model:{} by {} has {} cores {}. It has a base clock of {}Ghz and boost clock of {}Ghz, compatible with the socket {}. It is released on {} and it {}.'.format(
            self.model, self.manufacturer, self.core_count, hyperthread_description, self.clock_speed_ghz,
            self.boost_clock_ghz, self.socket, self.release_date, discontinued_description)
        return description

    def get_part_type(self):
        """Get Part type"""
        return Cpu.PART_TYPE

    def to_dict(self):
        """ Return dictionary of the part"""
        dict = {}
        dict['clock_speed_ghz'] = self.clock_speed_ghz
        dict['boost_clock_ghz'] = self.boost_clock_ghz
        dict['core_count'] = self.core_count
        dict['socket'] = self.socket
        dict['hyperthread'] = self.hyperthread
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
    def validate_clock(display_name, clock):
        """Validate the value of the clock speed variable """
        if (clock is None) or (isinstance(clock, (float, int)) is False) or (clock < Cpu.MIN_CLOCK):
            raise ValueError(display_name + ' you have entered is invalid')

    @staticmethod
    def validate_bool(display_name, bool_input):
        if (type(bool_input) != bool) or (bool_input is None):
            raise ValueError(display_name + ' you have entered is invalid')

    @staticmethod
    def validate_core(display_name, int_input):
        if (isinstance(int_input, (float, int)) is False) or (int_input is None) or (int_input < Cpu.MIN_CORE):
            raise ValueError(display_name + ' you have entered is invalid')

