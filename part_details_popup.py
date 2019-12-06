import tkinter as tk
from tkinter import messagebox
import requests
import re


class DetailsPopup(tk.Frame):
    """ Popup Frame to Complete a Repair """

    def __init__(self, parent, info, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        index = 0
        for k, v in info:
            if (k == 'hyperthread') and (v == 1):
                tk.Label(self, text=str(k) + ' : ' + 'True').grid(row=1 + index, column=2)
            elif (k == 'hyperthread') and (v == 0):
                tk.Label(self, text=str(k) + ' : ' + 'False').grid(row=1 + index, column=2)
            elif (k == 'is_discontinued') and (v == 1):
                tk.Label(self, text='Discontinued' + ' : ' + 'True').grid(row=1 + index, column=2)
            elif (k == 'is_discontinued') and (v == 0):
                tk.Label(self, text='Discontinued' + ' : ' + 'False').grid(row=1 + index, column=2)
            else:
                tk.Label(self, text=str(k) + ' : ' + str(v)).grid(row=1+index, column=2)
            index += 1

