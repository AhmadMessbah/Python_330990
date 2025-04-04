from tkinter import *
import tkinter.ttk as ttk


class Table:
    def table_select(self, event):
        row_id = self.table.focus()
        item = self.table.item(row_id)["values"]
        if self.function_name:
            self.function_name(item)

    def clear_table(self):
        for item in self.table.get_children():
            self.table.delete(item)

    def show_data(self, data_list):
        for data in data_list:
            self.table.insert("", END, values=data)

    def __init__(self, window, columns_count, headings, column_widths, x, y, height=10, function_name=None):
        self.function_name = function_name
        columns = list(range(columns_count))
        self.table = ttk.Treeview(window, columns=columns, height=height, show="headings")

        for col in columns:
            self.table.heading(col, text=headings[col])
            self.table.column(col, width=column_widths[col])

        self.table.place(x=x, y=y)

        self.table.bind("<<TreeviewSelect>>", self.table_select)
