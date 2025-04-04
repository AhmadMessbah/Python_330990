from tkinter import *
import tkinter.messagebox as msg

from controller.customer_controller import CustomerController
from view.component.label_and_entry import LabelAndEntry
from view.component.table import Table

from model.customer import Customer


class CustomerView:
    def save_click(self):
        status, message = self.controller.save(
            self.first_name.get(),
            self.family_name.get(),
            self.gender.get(),
            self.phone.get(),
            self.birth_date.get(),
            self.medical_history.get()
        )
        if status:
            msg.showinfo("Saved", message)
        else:
            msg.showerror("Error", message)
        self.reset_form()

    def edit_click(self):
        status, message = self.controller.edit(
            self.id.get(),
            self.first_name.get(),
            self.family_name.get(),
            self.gender.get(),
            self.phone.get(),
            self.birth_date.get(),
            self.medical_history.get()
        )
        if status:
            msg.showinfo("Edited", message)
        else:
            msg.showerror("Error", message)
        self.reset_form()

    def remove_click(self):
        status, message = self.controller.remove(self.id.get())
        if status:
            msg.showinfo("Removed", message)
        else:
            msg.showerror("Error", message)
        self.reset_form()

    def reset_form(self):
        self.id.set(0)
        self.first_name.set("")
        self.family_name.set("")
        self.gender.set("")
        self.phone.set("")
        self.birth_date.set("")
        self.medical_history.set("")
        self.table.clear_table()
        self.table.show_data(self.controller.find_all())

    def select_table(self, selected_row):
        customer = Customer(*selected_row)
        self.id.set(customer.id)
        self.first_name.set(customer.first_name)
        self.family_name.set(customer.family_name)
        self.gender.set(customer.gender)
        self.phone.set(customer.phone)
        self.birth_date.set(customer.birth_date)
        self.medical_history.set(customer.medical_history)

    def __init__(self):
        self.controller = CustomerController()

        self.win = Tk()
        self.win.geometry("850x400")
        self.win.title("Customer View")

        self.id = LabelAndEntry(self.win, "Id", 20, 20, IntVar, 90, state="readonly")
        self.first_name = LabelAndEntry(self.win, "First Name", 20, 60, StringVar, 90)
        self.family_name = LabelAndEntry(self.win, "Family Name", 20, 100, StringVar, 90)
        self.gender = LabelAndEntry(self.win, "Gender", 20, 140, StringVar, 90)
        self.phone = LabelAndEntry(self.win, "Phone", 20, 180, StringVar, 90)
        self.birth_date = LabelAndEntry(self.win, "Birth Date", 20, 220, StringVar, 90)
        self.medical_history = LabelAndEntry(self.win, "Medical History", 20, 260, StringVar, 90)

        Button(self.win, text="Save", width=7, command=self.save_click).place(x=20, y=330)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=85, y=330)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=150, y=330)

        self.table = Table(
            self.win,
            7,
            ["Id", "First Name", "Family Name", "Gender", "Phone", "Birth Date", "Medical History"],
            [60, 100, 100, 70, 120, 100, 150],
            230, 20,
            13,
            self.select_table
        )

        self.reset_form()

        self.win.mainloop()
