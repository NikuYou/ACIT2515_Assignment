import tkinter as tk
from tkinter import messagebox
import requests
import re
import json


class UpdatePopup(tk.Frame):
    """ Popup Frame to Complete a Repair """

    def __init__(self, parent, model_string, close_callback):
        """ Constructor """
        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)
        self._is_discontinued = tk.BooleanVar()

        tk.Label(self, text="Model:").grid(row=1, column=1)
        tk.Label(self, text="Stock:").grid(row=2, column=1)
        tk.Label(self, text="is_discontinued:").grid(row=3, column=1)

        selected_model = tk.StringVar(self, value=model_string)
        self._model = tk.Entry(self, textvariable=selected_model)
        self._model.grid(row=1, column=3)
        self._stock = tk.Entry(self)
        self._stock.grid(row=2, column=3)
        self._is_discontinued_yes = tk.Radiobutton(self, text="Yes", value=True,
                                                   variable=self._is_discontinued)
        self._is_discontinued_yes.grid(row=3, column=2)
        self._is_discontinued_no = tk.Radiobutton(self, text="No", value=False,
                                                  variable=self._is_discontinued)
        self._is_discontinued_no.grid(row=3, column=3)
        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=5, column=2)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=5, column=3)

    def _submit_cb(self):
        """ Submit Complete Repair """
        if re.match("^[0-9]\d{0,9}$", self._stock.get()) is None:
            messagebox.showerror("Error", "Stock must be a valid integer")
            return
        # Create the dictionary for the JSON request body
        data = {}
        data['model'] = self._model.get()
        data['stock'] = int(self._stock.get())
        data['is_discontinued'] = self._is_discontinued.get()

        # Implement your code here
        headers = {"content-type": "application/json"}
        response = requests.put("http://127.0.0.1:5000/compshop/parts/update", json=data,
                                headers=headers)

        if response.status_code == 200:
            self._close_cb()
        else:
            messagebox.showerror("Error", "Complete Repair Request Failed")
