import tkinter as tk
from tkinter import messagebox
import requests
from add_cpu_popup import AddCpuPopup
from add_gpu_popup import AddGpuPopup
from update_popup import UpdatePopup
from part_details_popup import DetailsPopup


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)
        self.pack(padx=20, pady=20)
        tk.Label(self, text="Parts in Shop").grid(row=1, column=2)
        self._parts_listbox = tk.Listbox(self, width=160)
        self._parts_listbox.grid(row=2, column=1, rowspan=7, columnspan=5)
        self._parts_listbox.bind("<Double-Button-1>", self._call_details)

        self._part_toggle = tk.BooleanVar()
        tk.Label(self, text="Parts:").grid(row=1, column=3)
        self._part_toggle_yes = tk.Radiobutton(self, text="CPU", value=True,
                                               variable=self._part_toggle)
        self._part_toggle_yes.grid(row=1, column=4)
        self._part_toggle_no = tk.Radiobutton(self, text="GPU", value=False,
                                              variable=self._part_toggle)
        self._part_toggle_no.grid(row=1, column=5)
        self._part_toggle_yes.bind("<Button-1>", self._call_back)
        self._part_toggle_no.bind("<Button-1>", self._call_back)

        tk.Button(self, text="Add Cpu", command=self._add_cpu).grid(row=10, column=1)
        tk.Button(self, text="Add Gpu", command=self._add_gpu).grid(row=10, column=2)
        tk.Button(self, text="Update Part", command=self._call_update).grid(row=10, column=3)
        tk.Button(self, text="Remove Part", command=self._remove_part).grid(row=10, column=4)
        tk.Button(self, text="Quit", command=self._quit_callback).grid(row=10, column=5)

        tk.Label(self, text="Total models of parts:").grid(row=2, column=6)
        tk.Label(self, text="Number of CPU Models:").grid(row=3, column=6)
        tk.Label(self, text="Number of GPU Models:").grid(row=4, column=6)
        tk.Label(self, text="Total number of Stock:").grid(row=5, column=6)
        tk.Label(self, text="Number of CPU stock:").grid(row=6, column=6)
        tk.Label(self, text="Number of GPU stock:").grid(row=7, column=6)
        tk.Label(self, text="Number of Discontinued parts' Stock:").grid(row=8, column=6)

        self._update_parts_list()

    def _add_cpu(self):
        """ Add Cpu Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddCpuPopup(self._popup_win, self._close_cpu_cb)

    def _close_cpu_cb(self):
        """ Close Add Phone Popup """
        self._popup_win.destroy()
        self._update_parts_list()

    def _add_gpu(self):
        """ Add Tablet Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddGpuPopup(self._popup_win, self._close_gpu_cb)

    def _close_gpu_cb(self):
        """ Close Add Tablet Popup """
        self._popup_win.destroy()
        self._update_parts_list()

    def _remove_part(self):
        """ Remove Device Popup """
        self.zones = self._parts_listbox.curselection()
        response_parts = requests.get("http://127.0.0.1:5000/compshop/parts/all")
        if response_parts.status_code != 200:
            messagebox.showwarning("Warning", "Could not retrieve the parts.")
            return
        part_list = response_parts.json()
        selected_part = part_list[self.zones[0]].items()
        for k, v in selected_part:
            if k == 'model':
                model_string = v

        MsgBox = tk.messagebox.askquestion('Confirm Delete',
                                           'Are you sure you want to remove: ' + model_string,
                                           icon='warning')
        if MsgBox == 'yes':
            pass
        else:
            return

        headers = {"content-type": "application/json"}
        response = requests.delete("http://127.0.0.1:5000/compshop/parts/"+model_string,
                                   json={},
                                   headers=headers)

        if response.status_code != 200:
            messagebox.showerror("Error", "Remove Parts Request Failed")
        else:
            messagebox.showinfo("Success", "Parts removed from Database")
            self._update_parts_list()

    def _quit_callback(self):
        """ Quit """
        self.quit()

    def _update_parts_list(self):
        """ Update the List of Device Descriptions """
        if self._part_toggle.get() is not True:
            response_parts = requests.get("http://127.0.0.1:5000/compshop/parts/all/cpu")
        else:
            response_parts = requests.get("http://127.0.0.1:5000/compshop/parts/all/gpu")

        if response_parts.status_code != 200:
            messagebox.showwarning("Warning", "Could not retrieve the parts.")
            return

        self._parts_listbox.delete(0, tk.END)
        parts_descs = response_parts.json()

        for parts_desc in parts_descs:
            self._parts_listbox.insert(tk.END, parts_desc)

        response_stat = requests.get(
            "http://127.0.0.1:5000/compshop/shopstats")
        if response_stat.status_code != 200:
            messagebox.showwarning("Warning", "Could not retrieve shop stats.")
            return
        stats = response_stat.json()
        tk.Label(self, text=stats['total_parts_model']).grid(row=2, column=7)
        tk.Label(self, text=stats['num_cpu_model']).grid(row=3, column=7)
        tk.Label(self, text=stats['num_gpu_model']).grid(row=4, column=7)
        tk.Label(self, text=stats['total_stock']).grid(row=5, column=7)
        tk.Label(self, text=stats['num_cpu_stock']).grid(row=6, column=7)
        tk.Label(self, text=stats['num_gpu_stock']).grid(row=7, column=7)
        tk.Label(self, text=stats['discontinued_stock']).grid(row=8, column=7)

    def _call_details(self, event):
        self.zones = self._parts_listbox.curselection()
        response_parts = requests.get("http://127.0.0.1:5000/compshop/parts/all")
        if response_parts.status_code != 200:
            messagebox.showwarning("Warning", "Could not retrieve the parts.")
            return
        part_list = response_parts.json()
        parts = []
        if self._part_toggle.get() is True:
            for i in part_list:
                if i['type'] == 'CPU':
                    parts.append(i)
        else:
            for i in part_list:
                if i['type'] == 'GPU':
                    parts.append(i)

        selected_part = parts[self.zones[0]].items()
        self._part_details(selected_part)

    def _call_back(self, event):
        self._update_parts_list()

    def _part_details(self, info):
        """ Part Details Popup """
        self._popup_win = tk.Toplevel()
        self._popup = DetailsPopup(self._popup_win, info, self._close_detail)

    def _close_detail(self):
        """ Close Detail Popup """
        self._popup_win.destroy()
        self._update_parts_list()

    def _call_update(self):
        self.zones = self._parts_listbox.curselection()
        response_parts = requests.get("http://127.0.0.1:5000/compshop/parts/all")
        if response_parts.status_code != 200:
            messagebox.showwarning("Warning", "Could not retrieve the parts.")
            return
        part_list = response_parts.json()
        parts = []
        if self._part_toggle.get() is True:
            for i in part_list:
                if i['type'] == 'CPU':
                    parts.append(i)
        else:
            for i in part_list:
                if i['type'] == 'GPU':
                    parts.append(i)

        selected_part = parts[self.zones[0]].items()
        for k, v in selected_part:
            if k == 'model':
                model_string = v
        self._update_part(model_string)

    def _update_part(self, part):
        """ Complete Repair Popup """
        self._popup_win = tk.Toplevel()
        self._popup = UpdatePopup(self._popup_win, part, self._close_update_cb)

    def _close_update_cb(self):
        """ Close Complete Repair Popup """
        self._popup_win.destroy()
        self._update_parts_list()


if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()

