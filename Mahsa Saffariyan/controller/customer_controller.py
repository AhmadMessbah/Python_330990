from model.customer import Customer
from service.customer_service import CustomerService
from validation.validator import customer_validator


def error_handler(my_function):
    def inner(*args, **kwargs):
        try:
            result = my_function(*args, **kwargs)
            return True, result
        except Exception as e:
            return False, e

    return inner


class CustomerController:
    def __init__(self):
        self.service = CustomerService()

    @error_handler
    def save(self, first_name, family_name, gender, phone, birth_date, medical_history):
        customer = Customer(None, first_name, family_name, gender, phone, birth_date, medical_history)
        errors = customer_validator(customer)
        if errors:
            raise Exception(errors)
        self.service.save(customer)
        return "Customer Saved"

    @error_handler
    def edit(self, customer_id, first_name, family_name, gender, phone, birth_date, medical_history):
        customer = Customer(customer_id, first_name, family_name, gender, phone, birth_date, medical_history)
        errors = customer_validator(customer)
        if errors:
            raise Exception(errors)
        self.service.edit(customer)
        return "Customer Edited"

    @error_handler
    def remove(self, customer_id):
        self.service.remove(customer_id)
        return "Customer Removed"

    @error_handler
    def find_all(self):
        return self.service.find_all()
