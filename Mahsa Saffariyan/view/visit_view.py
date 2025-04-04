from tkinter import *
import tkinter.messagebox as msg

from controller.visit_controller import VisitController
from view.component.label_and_entry import LabelAndEntry
from view.component.table import Table

from model.visit import Visit


class VisitView:
    def save_click(self):
        status, message = self.controller.book_visit(
            self.customer_id.get(),
            self.schedule_id.get(),
            self.reason.get(),
            self.fee.get(),
            self.visit_status.get()
        )
        if status:
            msg.showinfo("Saved", message)
        else:
            msg.showerror("Error", message)
        self.reset_form()

    def reset_form(self):
        self.customer_id.set(0)
        self.schedule_id.set(0)
        self.reason.set("")
        self.fee.set(0.0)
        self.visit_status.set("")
        self.table.clear_table()
        self.table.show_data(self.controller.find_all())

    def select_table(self, selected_row):
        visit = Visit(*selected_row)
        self.customer_id.set(visit.customer_id)
        self.schedule_id.set(visit.schedule_id)
        self.reason.set(visit.reason)
        self.fee.set(visit.fee)
        self.visit_status.set(visit.visit_status)

    def __init__(self):
        self.controller = VisitController()

        self.win = Tk()
        self.win.geometry("850x350")
        self.win.title("Visit View")

        self.customer_id = LabelAndEntry(self.win, "Customer Id", 20, 20, IntVar, 90)
        self.schedule_id = LabelAndEntry(self.win, "Schedule Id", 20, 60, IntVar, 90)
        self.reason = LabelAndEntry(self.win, "Reason", 20, 100, StringVar, 90)
        self.fee = LabelAndEntry(self.win, "Fee", 20, 140, DoubleVar, 90)
        self.visit_status = LabelAndEntry(self.win, "Visit Status", 20, 180, StringVar, 90)

        Button(self.win, text="Save", width=7, command=self.save_click).place(x=20, y=260)

        self.table = Table(
            self.win,
            5,
            ["Customer Id", "Schedule Id", "Reason", "Fee", "Visit Status"],
            [100, 100, 150, 80, 100],
            230, 20,
            13,
            self.select_table
        )

        self.reset_form()

        self.win.mainloop()
