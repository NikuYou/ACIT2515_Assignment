from abstract_part import AbstractPart


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

    def __init__(self, clock_speed_mhz, boost_clock_mhz, chipset, pcie_ver, length_cm, thickness_cm,
                 model, manufacturer, price, cost, stock, release_date_input, ID=0,
                 is_discontinued=False):
        """Initialize Gpu"""

        Gpu._validate_pos_float(Gpu.CLOCK_DISPLAY, clock_speed_mhz)
        Gpu._validate_pos_float(Gpu.BOOST_DISPLAY, boost_clock_mhz)
        Gpu._validate_string(Gpu.CHIPSET_DISPLAY, chipset)
        Gpu._validate_pos_float(Gpu.PCIE_VER__DISPLAY, pcie_ver)
        Gpu._validate_pos_float(Gpu.LENGTH_DISPLAY, length_cm)
        Gpu._validate_pos_float(Gpu.THICKNESS_DISPLAY, thickness_cm)

        self._clock_speed_mhz = float("%.2f" % clock_speed_mhz)
        self._boost_clock_mhz = float("%.2f" % boost_clock_mhz)
        self._chipset = chipset
        self._pcie_ver = float("%.1f" % pcie_ver)
        self._length_cm = float("%.2f" % length_cm)
        self._thickness_cm = float("%.2f" % thickness_cm)

        super().__init__(model, manufacturer, price, cost, stock, release_date_input, ID,
                         is_discontinued)

    def get_clock_speed(self):
        """Get the clock speed(float) of the Gpu"""
        return self._clock_speed_mhz

    def get_boost_clock(self):
        """Get the boost clock(float) of the Gpu"""
        return self._boost_clock_mhz

    def get_chipset(self):
        """Get the chipset of the Gpu"""
        return self._chipset

    def get_length(self):
        """Get the length(float) of the GPU in cm"""
        return self._length_cm

    def get_thickness(self):
        """Get the thickness(float) of the GPU in cm"""
        return self._thickness_cm

    def get_description(self):
        """get Part description"""
        if self._is_discontinued is True:
            discontinued_description = 'is discontinued'
        else:
            discontinued_description = 'is not discontinued'
        description = 'The GPU model:{} by {} has a base clock of {}Mhz and boost clock of {}Mhz. It runs on PCIE{}. It has length:{}cm and thickness:{}cm.  It is released on {} and it {}.'.format(
            self._model, self._manufacturer, self._clock_speed_mhz,
            self._boost_clock_mhz, self._pcie_ver, self._length_cm, self._thickness_cm,
            self._release_date,
            discontinued_description)
        return description

    def get_part_type(self):
        """Get Part type"""
        return Gpu.PART_TYPE

    @staticmethod
    def _validate_string(display_name, str_input):
        if str_input is None:
            raise ValueError(display_name + ' cannot be undefined.')
        elif type(str_input) != str:
            raise ValueError(display_name + ' has to be a string.')
        elif str_input == "":
            raise ValueError(display_name + ' cannot be empty.')

    @staticmethod
    def _validate_pos_float(display_name, clock):
        """Validate the value of the clock speed variable """
        if (clock is None) or (isinstance(clock, (float, int)) is False) or (
                clock < Gpu.MIN_CLOCK_PCIE_LENGTH_THICKNESS):
            raise ValueError(display_name + ' you have entered is invalid')
