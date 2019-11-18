class ShopStats:
    """ Statistics on Computer Parts Shop Inventory """

    def __init__(self, total_parts_model, num_cpu_model, num_gpu_model, total_stock, num_cpu_stock, num_gpu_stock, discontinued_stock):
        """ Initialize the data values """

        if total_parts_model is None or type(total_parts_model) != int:
            raise ValueError("Invalid total number of parts model value")
        self._total_parts_model = total_parts_model

        if num_cpu_model is None or type(num_cpu_model) != int:
            raise ValueError("Invalid number of CPU model value")
        self._num_cpu_model = num_cpu_model

        if num_gpu_model is None or type(num_gpu_model) != int:
            raise ValueError("Invalid number of GPU model value")
        self._num_gpu_model = num_gpu_model

        if total_stock is None or type(total_stock) != int:
            raise ValueError("Invalid total number of stock value")
        self._total_stock = total_stock

        if num_cpu_stock is None or type(num_cpu_stock) != int:
            raise ValueError("Invalid number of CPU stock value")
        self._num_cpu_stock = num_cpu_stock

        if num_gpu_stock is None or type(num_gpu_stock) != int:
            raise ValueError("Invalid number of GPU stock value")
        self._num_gpu_stock = num_gpu_stock

        if discontinued_stock is None or type(discontinued_stock) != int:
            raise ValueError("Invalid number of discontinued stock value")
        self._discontinued_stock = discontinued_stock

    def get_total_parts_model(self):
        """ Returns the total number of parts model """
        return self._total_parts_model

    def get_num_cpu_model(self):
        """ Returns the number cf CPU model """
        return self._num_cpu_model

    def get_num_gpu_model(self):
        """ Returns the number cf GPU model """
        return self._num_gpu_model

    def get_total_stock(self):
        """ Returns the total number of parts in stock """
        return self._total_stock

    def get_num_cpu_stock(self):
        """ Returns the total number of CPU in stock """
        return self._num_cpu_stock

    def get_num_gpu_stock(self):
        """ Returns the total number of GPU in stock """
        return self._num_gpu_stock

    def get_discontinued_stock(self):
        """ Returns the total number of discontinued parts in stock """
        return self._discontinued_stock

    def to_dict(self):
        """ Return dictionary of the part"""
        dict = {}
        dict['total_parts_model'] = self._total_parts_model
        dict['num_cpu_model'] = self._num_cpu_model
        dict['num_gpu_model'] = self._num_gpu_model
        dict['total_stock'] = self._total_stock
        dict['num_cpu_stock'] = self._num_cpu_stock
        dict['num_gpu_stock'] = self._num_gpu_stock
        dict['discontinued_stock'] = self._discontinued_stock
        return dict
