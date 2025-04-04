from datetime import date

from controller.customer_controller import CustomerController
from model.customer import Customer
from repository.customer_repository import CustomerRepository
from validation.validator import customer_validator

customer_controller = CustomerController()
print(customer_controller.save("Mahsa", "Shirazi", date(1995, 6, 15), "ms123", "09123456789"))

# repo = CustomerRepository()
# customer = Customer(1, 'Reza', 'Amiri', 'Male', '09123456789', '1990-08-12')

# Test Passed
# repo.save(customer)

# Test Passed
# print(customer_validator(customer))
# repo.edit(customer)

# Test Passed
# repo.remove(1)

# Test Passed
# print(repo.find_all())

# Test Passed
# print(repo.find_by_id(1))

# Test Passed
# print(repo.find_by_name_and_family('Reza', 'Amiri'))
