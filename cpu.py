from abstract_part import AbstractPart


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

    def __init__(self, clock_speed_ghz, boost_clock_ghz, core_count, socket, hyperthread, model,
                 manufacturer, price, cost, stock, release_date_input, ID=0, is_discontinued=False):
        """Initialize Cpu"""

        Cpu._validate_clock(Cpu.CLOCK_DISPLAY, clock_speed_ghz)
        Cpu._validate_clock(Cpu.BOOST_DISPLAY, boost_clock_ghz)
        Cpu._validate_core(Cpu.CORE_COUNT_DISPLAY, core_count)
        Cpu._validate_string(Cpu.SOCKET_DISPLAY, socket)
        Cpu._validate_bool(Cpu.HYPERTHREAD_DISPLAY, hyperthread)

        self._clock_speed_ghz = float("%.2f" % clock_speed_ghz)
        self._boost_clock_ghz = float("%.2f" % boost_clock_ghz)
        self._core_count = core_count
        self._socket = socket
        self._hyperthread = hyperthread

        super().__init__(model, manufacturer, price, cost, stock, release_date_input, ID,
                         is_discontinued)

    def get_clock_speed(self):
        """Get the clock speed(float) of the Cpu"""
        return self._clock_speed_ghz

    def get_boost_clock(self):
        """Get the boost clock(float) of the Cpu"""
        return self._boost_clock_ghz

    def get_core_count(self):
        """Get the core count(int) of the Cpu"""
        return self._core_count

    def get_hyperthread(self):
        """Get the Hyperthreading availability status (Boolean)"""
        return self._hyperthread

    def get_description(self):
        """get Part description"""
        if self._hyperthread is True:
            hyperthread_description = 'with hyperthreading'
        else:
            hyperthread_description = 'with no hyperthreading'
        if self._is_discontinued is True:
            discontinued_description = 'is discontinued'
        else:
            discontinued_description = 'is not discontinued'
        description = 'The CPU model:{} by {} has {} cores {}. It has a base clock of {}Ghz and boost clock of {}Ghz, compatible with the socket {}. It is released on {} and it {}.'.format(
            self._model, self._manufacturer, self._core_count, hyperthread_description,
            self._clock_speed_ghz,
            self._boost_clock_ghz, self._socket, self._release_date, discontinued_description)
        return description

    def get_part_type(self):
        """Get Part type"""
        return Cpu.PART_TYPE

    @staticmethod
    def _validate_string(display_name, str_input):
        if str_input is None:
            raise ValueError(display_name + ' cannot be undefined.')
        elif type(str_input) != str:
            raise ValueError(display_name + ' has to be a string.')
        elif str_input == "":
            raise ValueError(display_name + ' cannot be empty.')

    @staticmethod
    def _validate_clock(display_name, clock):
        """Validate the value of the clock speed variable """
        if (clock is None) or (isinstance(clock, (float, int)) is False) or (clock < Cpu.MIN_CLOCK):
            raise ValueError(display_name + ' you have entered is invalid')

    @staticmethod
    def _validate_bool(display_name, bool_input):
        if (type(bool_input) != bool) or (bool_input is None):
            raise ValueError(display_name + ' you have entered is invalid')

    @staticmethod
    def _validate_core(display_name, int_input):
        if (isinstance(int_input, (float, int)) is False) or (int_input is None) or (
                int_input < Cpu.MIN_CORE):
            raise ValueError(display_name + ' you have entered is invalid')
