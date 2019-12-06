import tkinter as tk
from tkinter import messagebox
import requests
import re


class AddGpuPopup(tk.Frame):
    """ Popup Frame to Add a Tablet """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)
        self._hyperthread = tk.BooleanVar()

        tk.Label(self, text="Model:").grid(row=1, column=1)
        self._model = tk.Entry(self)
        self._model.grid(row=1, column=3)
        tk.Label(self, text="Manufacturer:").grid(row=2, column=1)
        self._manufacturer = tk.Entry(self)
        self._manufacturer.grid(row=2, column=3)
        tk.Label(self, text="Clock Speed(Mhz):").grid(row=3, column=1)
        self._clock_speed_mhz = tk.Entry(self)
        self._clock_speed_mhz.grid(row=3, column=3)
        tk.Label(self, text="Boost Clock(Mhz):").grid(row=4, column=1)
        self._boost_clock_mhz = tk.Entry(self)
        self._boost_clock_mhz.grid(row=4, column=3)
        tk.Label(self, text="PCIE Version:").grid(row=5, column=1)
        self._pcie_ver = tk.Entry(self)
        self._pcie_ver.grid(row=5, column=3)
        tk.Label(self, text="Chipset:").grid(row=6, column=1)
        self._chipset = tk.Entry(self)
        self._chipset.grid(row=6, column=3)
        tk.Label(self, text="Price:").grid(row=7, column=1)
        self._sale_price = tk.Entry(self)
        self._sale_price.grid(row=7, column=3)
        tk.Label(self, text="Cost:").grid(row=8, column=1)
        self._cost = tk.Entry(self)
        self._cost.grid(row=8, column=3)
        tk.Label(self, text="Stock:").grid(row=9, column=1)
        self._stock = tk.Entry(self)
        self._stock.grid(row=9, column=3)
        tk.Label(self, text="Release Date:").grid(row=10, column=1)
        self._release_date = tk.Entry(self)
        self._release_date.grid(row=10, column=3)
        tk.Label(self, text="length(cm):").grid(row=11, column=1)
        self._length_cm = tk.Entry(self)
        self._length_cm.grid(row=11, column=3)
        tk.Label(self, text="thickness(cm):").grid(row=12, column=1)
        self._thickness_cm = tk.Entry(self)
        self._thickness_cm.grid(row=12, column=3)

        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=13, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=13, column=3)

    def _submit_cb(self):
        """ Submit the Add Tablet """

        # Validate the non-string data values
        if re.match("^\d{4}-\d{2}-\d{2}$", self._release_date.get()) is None:
            messagebox.showerror("Error", "Release date must have format yyyy-mm-dd")
            return

        if re.match("^\d+$", self._pcie_ver.get()) is None:
            messagebox.showerror("Error", "PCIE Version must be a valid integer")
            return

        if re.match("^\d+$", self._stock.get()) is None:
            messagebox.showerror("Error", "Stock number must be a valid integer")
            return

        if re.match("^\d+.\d{2}$", self._sale_price.get()) is None:
            messagebox.showerror("Error", "Sale price must be a valid price")
            return

        if re.match("^\d+.\d{2}$", self._cost.get()) is None:
            messagebox.showerror("Error", "Cost must be a valid price")
            return

        if re.match("^\d+.\d{2}$", self._clock_speed_mhz.get()) is None:
            messagebox.showerror("Error", "Clock Speed must have 2 decimal place.")
            return

        if re.match("^\d+.\d{2}$", self._boost_clock_mhz.get()) is None:
            messagebox.showerror("Error", "Boost clock must have 2 decimal place.")
            return

        if re.match("^\d+.\d{2}$", self._length_cm.get()) is None:
            messagebox.showerror("Error", "Length must have 2 decimal place.")
            return

        if re.match("^\d+.\d{2}$", self._thickness_cm.get()) is None:
            messagebox.showerror("Error", "Thickness must have 2 decimal place.")
            return



        # Create the dictionary for the JSON request body
        data = {}
        data['manufacturer'] = self._manufacturer.get()
        data['chipset'] = self._chipset.get()
        data['model'] = self._model.get()
        data['pcie_ver'] = int(self._pcie_ver.get())
        data['stock'] = int(self._stock.get())
        data['price'] = float(self._sale_price.get())
        data['cost'] = float(self._cost.get())
        data['release_date'] = self._release_date.get()
        data['clock_speed_mhz'] = float(self._clock_speed_mhz.get())
        data['boost_clock_mhz'] = float(self._boost_clock_mhz.get())
        data['length_cm'] = float(self._length_cm.get())
        data['thickness_cm'] = float(self._thickness_cm.get())
        data['type'] = "GPU"

        # Implement your code here
        """ Adds a point to the backend grid """
        headers = {"content-type": "application/json"}
        response = requests.post("http://127.0.0.1:5000/compshop/parts", json=data,
                                 headers=headers)

        if response.status_code == 200:
            messagebox.showinfo("Success", "GPU added to Database")
            self._close_cb()
        else:
            messagebox.showerror("Error", "Add GPU Request Failed")

