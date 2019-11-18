# Bryan Yuen A01160576
from datetime import datetime


class AbstractPart:
    """AbstractMobileDevice Class"""
    MIN_MONEY = 0
    MIN_STOCK = 0
    ID_DISPLAY = "ID"
    MANUFACTURER_DISPLAY = "Manufacturer"
    MODEL_DISPLAY = "Model"
    PRICE_DISPLAY = "Price"
    COST_DISPLAY = "Cost"
    DISCONTINUED_DISPLAY = "Discontinued Status"

    def __init__(self, model, manufacturer, price, cost, stock, release_date_input, id=0, is_discontinued=False):
        """Initialize AbstractPart"""
        if release_date_input != '' and (release_date_input is not None) and (type(release_date_input) != datetime):
            release_date = datetime.strptime(release_date_input, '%Y-%m-%d')
        elif type(release_date_input) == datetime:
            release_date = release_date_input
        else:
            raise ValueError('The release date cannot be empty or undefined.')

        AbstractPart._validate_int(AbstractPart.ID_DISPLAY, id)
        AbstractPart._validate_string(AbstractPart.MANUFACTURER_DISPLAY, manufacturer)
        AbstractPart._validate_string(AbstractPart.MODEL_DISPLAY, model)
        AbstractPart._validate_money(AbstractPart.PRICE_DISPLAY, price)
        AbstractPart._validate_money(AbstractPart.COST_DISPLAY, cost)
        AbstractPart._validate_stock(stock)
        AbstractPart._validate_datetime(release_date)

        self._id = int(id)
        self._manufacturer = manufacturer
        self._model = model
        self._stock = int(stock)
        self._release_date = release_date
        self._is_discontinued = is_discontinued
        self._cost = float("%.2f" % cost)
        self._price = float("%.2f" % price)

    def get_cost(self):
        """get the cost of part"""
        return float("%.2f" % self._cost)

    def calc_profit(self):
        """Calculate and return the profit of selling one of this part"""
        profit = float("%.2f" % self._price) - float("%.2f" % self._cost)
        return float("%.2f" % profit)

    def _set_price(self, price):
        """set the price of part"""
        AbstractPart._validate_money(AbstractPart.PRICE_DISPLAY, price)
        self._price = float("%.2f" % price)

    def _get_price(self):
        """get the price of part"""
        return float("%.2f" % self._price)

    def _set_id(self, id):
        """set the id of part"""
        AbstractPart._validate_int(AbstractPart.ID_DISPLAY, id)
        self._id = id

    def _get_id(self):
        """get the id of part"""
        return self._id

    def get_stock(self):
        """get the stock number of part"""
        return self._stock

    def add_stock(self, stock_to_add):
        """increase the stock of part"""
        AbstractPart._validate_stock(stock_to_add)
        current_stock = self._stock
        temp_stock = current_stock + stock_to_add
        self._stock = temp_stock

    def get_model(self):
        """get the model of the part"""
        return self._model

    def get_release_date(self):
        """get the release date of the part"""
        return self._release_date

    def set_is_discontinued(self, status):
        """set the boolean status of if the part is discontinued"""
        AbstractPart._validate_bool(AbstractPart.DISCONTINUED_DISPLAY, status)
        self._is_discontinued = status

    def is_discontinued(self):
        """get the boolean status of if the part is discontinued"""
        return self._is_discontinued

    def get_description(self):
        """get device description"""
        raise NotImplementedError("You must assign a child class first")

    def get_part_type(self):
        """get part type"""
        raise NotImplementedError("You must assign a child class first")

    def to_dict(self):
        """ Return dictionary of the part"""
        raise NotImplementedError("Subclass must implement abstract method")

    price = property(_get_price, _set_price)
    id = property(_get_id, _set_id)

    @staticmethod
    def _validate_money(display_name, money):
        """Validate the value of the monetary variable """
        if (money is None) or (isinstance(money, (float, int)) is False) or (money < AbstractPart.MIN_MONEY):
            raise ValueError(display_name + ' you have entered is invalid')

    @staticmethod
    def _validate_stock(stock):
        """Validate the value of the variable 'stock'"""
        if (stock is None) or (isinstance(stock, (float, int)) is False) or (stock < AbstractPart.MIN_STOCK):
            raise ValueError('The stock value you have entered is invalid')

    @staticmethod
    def _validate_string(display_name, str_input):
        if str_input is None:
            raise ValueError(display_name + ' cannot be undefined.')
        elif type(str_input) != str:
            raise ValueError(display_name + ' has to be a string.')
        elif str_input == "":
            raise ValueError(display_name + ' cannot be empty.')

    @staticmethod
    def _validate_datetime(date_input):
        if (type(date_input) != datetime) or (date_input is None):
            raise ValueError('The date you have entered is invalid')

    @staticmethod
    def _validate_bool(display_name, bool_input):
        if (type(bool_input) != bool) or (bool_input is None):
            raise ValueError(display_name + ' you have entered is invalid')

    @staticmethod
    def _validate_int(display_name, int_input):
        if (isinstance(int_input, (float, int)) is False) or (int_input is None):
            raise ValueError(display_name + ' you have entered is invalid')
