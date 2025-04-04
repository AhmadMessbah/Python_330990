from repository.customer_repository import CustomerRepository
from model.customer import Customer


class CustomerService:
    def __init__(self):
        self.repo = CustomerRepository()

    def save(self, customer):
        self.repo.save(customer)

    def edit(self, customer):
        self.repo.edit(customer)

    def remove(self, customer_id):
        self.repo.remove(customer_id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self, customer_id):
        return self.repo.find_by_id(customer_id)

    def find_by_name_and_family(self, first_name, family_name):
        return self.repo.find_by_name_and_family(first_name, family_name)
