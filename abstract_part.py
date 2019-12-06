# Bryan Yuen A01160576
from datetime import datetime
from base import Base
from sqlalchemy import Column, String, Integer, Float, DateTime


class AbstractPart(Base):
    """AbstractMobileDevice Class"""
    MIN_MONEY = 0
    MIN_STOCK = 0
    ID_DISPLAY = "ID"
    MANUFACTURER_DISPLAY = "Manufacturer"
    MODEL_DISPLAY = "Model"
    PRICE_DISPLAY = "Price"
    COST_DISPLAY = "Cost"
    DISCONTINUED_DISPLAY = "Discontinued Status"

    BOOLEAN_TRUE = 1

    __tablename__ = "parts"

    id = Column(Integer, primary_key=True)
    manufacturer = Column(String(100))
    model = Column(String(100))
    sale_price = Column(Float)
    cost = Column(Float)
    stock = Column(Integer)
    release_date = Column(DateTime)
    is_discontinued = Column(Integer)
    type = Column(String(6))

    def __init__(self, model, manufacturer, sale_price, cost, stock, release_date_input, part_type, is_discontinued=False):
        """Create Instance of AbstractPart"""
        if release_date_input != '' and (release_date_input is not None) and (type(release_date_input) == str):
            release_date = datetime.strptime(release_date_input, '%Y-%m-%d')
        elif type(release_date_input) == datetime:
            release_date = release_date_input
        else:
            raise ValueError('The release date cannot be empty or undefined.')

        AbstractPart.validate_string(AbstractPart.MANUFACTURER_DISPLAY, manufacturer)
        AbstractPart.validate_string(AbstractPart.MODEL_DISPLAY, model)
        AbstractPart.validate_money(AbstractPart.PRICE_DISPLAY, sale_price)
        AbstractPart.validate_money(AbstractPart.COST_DISPLAY, cost)
        AbstractPart.validate_stock(stock)
        AbstractPart.validate_datetime(release_date)
        AbstractPart.validate_string("Part Type", part_type)

        self.type = part_type
        self.manufacturer = manufacturer
        self.model = model
        self.stock = int(stock)
        self.release_date = release_date
        self.is_discontinued = is_discontinued
        self.cost = float("%.2f" % cost)
        self.sale_price = float("%.2f" % sale_price)

    def calc_profit(self):
        """Calculate and return the profit of selling one of this part"""
        profit = float("%.2f" % self.sale_price) - float("%.2f" % self.cost)
        return float("%.2f" % profit)

    def add_stock(self, stock_to_add):
        """increase the stock of part"""
        AbstractPart.validate_stock(stock_to_add)
        current_stock = self.stock
        temp_stock = current_stock + stock_to_add
        self.stock = temp_stock

    def set_is_discontinued(self, status):
        """set the boolean status of if the part is discontinued"""
        AbstractPart.validate_bool(AbstractPart.DISCONTINUED_DISPLAY, status)

        if status is True:
            self.is_discontinued = True
        else:
            self.is_discontinued = False

    def get_is_discontinued(self):
        """get the boolean status of if the part is discontinued"""
        if self.is_discontinued == AbstractPart.BOOLEAN_TRUE:
            return True
        return False

    def get_description(self):
        """get device description"""
        raise NotImplementedError("You must assign a child class first")

    def get_part_type(self):
        """get part type"""
        raise NotImplementedError("You must assign a child class first")

    def to_dict(self):
        """ Return dictionary of the part"""
        raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod
    def validate_money(display_name, money):
        """Validate the value of the monetary variable """
        if (money is None) or (isinstance(money, (float, int)) is False) or (money < AbstractPart.MIN_MONEY):
            raise ValueError(display_name + ' you have entered is invalid')

    @staticmethod
    def validate_stock(stock):
        """Validate the value of the variable 'stock'"""
        if (stock is None) or (isinstance(stock, (float, int)) is False) or (stock < AbstractPart.MIN_STOCK):
            raise ValueError('The stock value you have entered is invalid')

    @staticmethod
    def validate_string(display_name, str_input):
        if str_input is None:
            raise ValueError(display_name + ' cannot be undefined.')
        elif type(str_input) != str:
            raise ValueError(display_name + ' has to be a string.')
        elif str_input == "":
            raise ValueError(display_name + ' cannot be empty.')

    @staticmethod
    def validate_datetime(date_input):
        if (type(date_input) != datetime) or (date_input is None):
            raise ValueError('The date you have entered is invalid')

    @staticmethod
    def validate_bool(display_name, bool_input):
        if (type(bool_input) != bool) or (bool_input is None):
            raise ValueError(display_name + ' you have entered is invalid')

    @staticmethod
    def validate_int(display_name, int_input):
        if (isinstance(int_input, (float, int)) is False) or (int_input is None):
            raise ValueError(display_name + ' you have entered is invalid')

