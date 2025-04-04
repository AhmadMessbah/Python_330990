from tkinter import *
import tkinter.messagebox as msg

from controller.timing_controller import TimingController
from view.component.label_and_entry import LabelAndEntry
from view.component.table import Table

from model.timing import Timing


class TimingView:
    def save_click(self):
        status, message = self.controller.save(
            self.date.get(),
            self.start_time.get(),
            self.end_time.get(),
            self.status.get(),
            self.doctor_name.get()
        )
        if status:
            msg.showinfo("Saved", message)
        else:
            msg.showerror("Error", message)
        self.reset_form()

    def reset_form(self):
        self.date.set("")
        self.start_time.set("")
        self.end_time.set("")
        self.status.set("")
        self.doctor_name.set("")
        self.table.clear_table()
        self.table.show_data(self.controller.find_all())

    def select_table(self, selected_row):
        timing = Timing(*selected_row)
        self.date.set(timing.date)
        self.start_time.set(timing.start_time)
        self.end_time.set(timing.end_time)
        self.status.set(timing.status)
        self.doctor_name.set(timing.doctor_name)

    def __init__(self):
        self.controller = TimingController()

        self.win = Tk()
        self.win.geometry("900x350")
        self.win.title("Timing View")

        self.date = LabelAndEntry(self.win, "Date", 20, 20, StringVar, 90)
        self.start_time = LabelAndEntry(self.win, "Start Time", 20, 60, StringVar, 90)
        self.end_time = LabelAndEntry(self.win, "End Time", 20, 100, StringVar, 90)
        self.status = LabelAndEntry(self.win, "Status", 20, 140, StringVar, 90)
        self.doctor_name = LabelAndEntry(self.win, "Doctor Name", 20, 180, StringVar, 90)

        Button(self.win, text="Save", width=7, command=self.save_click).place(x=20, y=260)

        self.table = Table(
            self.win,
            5,
            ["Date", "Start Time", "End Time", "Status", "Doctor Name"],
            [100, 100, 100, 100, 150],
            230, 20,
            13,
            self.select_table
        )

        self.reset_form()

        self.win.mainloop()
