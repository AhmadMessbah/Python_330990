from tkinter import *

class LabelAndEntry:
    def __init__(self, window, text, x, y, variable_type=StringVar, distance=70, **kwargs):
        self.variable = variable_type()
        Label(window, text=text).place(x=x, y=y)
        Entry(window, textvariable=self.variable, **kwargs).place(x=x + distance, y=y)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)
