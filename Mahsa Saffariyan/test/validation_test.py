from model.customer import Customer
from model.timing import Timing
from model.visit import Visit
from validation.validator import customer_validator, timing_validator, visit_validator

# تست مشتری
customer1 = Customer(1, "Ali", "Alipour", "Male", "1234567890", "1990-01-01")
print("Customer Validation Errors:", customer_validator(customer1))

# تست زمان‌بندی
timing1 = Timing(1, "2025-04-05", "09:00", "10:00", "available", "Dr. Rezaee")
print("Timing Validation Errors:", timing_validator(timing1))

# تست ویزیت
visit1 = Visit(1, 1, 1, "Routine Checkup", 100, "Pending")
print("Visit Validation Errors:", visit_validator(visit1))
