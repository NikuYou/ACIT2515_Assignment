import tkinter as tk
from tkinter import messagebox
import requests
import re


class AddCpuPopup(tk.Frame):
    """ Popup Frame to Add a Phone """

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
        tk.Label(self, text="Clock Speed(Ghz):").grid(row=3, column=1)
        self._clock_speed_ghz = tk.Entry(self)
        self._clock_speed_ghz.grid(row=3, column=3)
        tk.Label(self, text="Boost Clock(Ghz):").grid(row=4, column=1)
        self._boost_clock_ghz = tk.Entry(self)
        self._boost_clock_ghz.grid(row=4, column=3)
        tk.Label(self, text="Core Count:").grid(row=5, column=1)
        self._core_count = tk.Entry(self)
        self._core_count.grid(row=5, column=3)
        tk.Label(self, text="Socket:").grid(row=6, column=1)
        self._socket = tk.Entry(self)
        self._socket.grid(row=6, column=3)
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

        tk.Label(self, text="hyperthread:").grid(row=11, column=1)
        self._hyperthread_yes = tk.Radiobutton(self, text="Yes", value=True,
                                                   variable=self._hyperthread)
        self._hyperthread_yes.grid(row=11, column=2)
        self._hyperthread_no = tk.Radiobutton(self, text="No", value=False,
                                                  variable=self._hyperthread)
        self._hyperthread_no.grid(row=11, column=3)
        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=12, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=12, column=3)

    def _submit_cb(self):
        """ Submit the Add Phone """

        # Validate the non-string data values
        if re.match("^\d{4}-\d{2}-\d{2}$", self._release_date.get()) is None:
            messagebox.showerror("Error", "Release date must have format yyyy-mm-dd")
            return

        if re.match("^\d+$", self._core_count.get()) is None:
            messagebox.showerror("Error", "Core Count must be a valid integer")
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

        if re.match("^\d+.\d{2}$", self._clock_speed_ghz.get()) is None:
            messagebox.showerror("Error", "Clock Speed must have 2 decimal place.")
            return

        if re.match("^\d+.\d{2}$", self._boost_clock_ghz.get()) is None:
            messagebox.showerror("Error", "Boost clock must have 2 decimal place.")
            return

        # Create the dictionary for the JSON request body
        data = {}
        data['manufacturer'] = self._manufacturer.get()
        data['socket'] = self._socket.get()
        data['model'] = self._model.get()
        data['core_count'] = int(self._core_count.get())
        data['stock'] = int(self._stock.get())
        data['price'] = float(self._sale_price.get())
        data['cost'] = float(self._cost.get())
        data['release_date'] = self._release_date.get()
        data['clock_speed_ghz'] = float(self._clock_speed_ghz.get())
        data['boost_clock_ghz'] = float(self._boost_clock_ghz.get())
        data['hyperthread'] = self._hyperthread.get()
        data['type'] = "CPU"

        # Implement your code here
        """ Adds a point to the backend grid """
        headers = {"content-type": "application/json"}
        response = requests.post("http://127.0.0.1:5000/compshop/parts", json=data, headers=headers)

        if response.status_code == 200:
            messagebox.showinfo("Success", "CPU added to Database")
            self._close_cb()
        else:
            messagebox.showerror("Error", "Add CPU Request Failed")

