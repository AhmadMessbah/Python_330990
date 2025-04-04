import re
from datetime import date, datetime


def customer_validator(customer):
    errors = []
    if not type(customer.first_name) == str or not re.match(r"^[a-zA-Z\s]{3,30}$", customer.first_name):
        errors.append({"field": "first_name", "message": "invalid first name"})

    if not type(customer.family_name) == str or not re.match(r"^[a-zA-Z\s]{3,30}$", customer.family_name):
        errors.append({"field": "family_name", "message": "invalid family name"})

    if not customer.gender in ["Male", "Female"]:
        errors.append({"field": "gender", "message": "invalid gender"})

    if not type(customer.phone) == str or not re.match(r"^\d{10}$", customer.phone):
        errors.append({"field": "phone", "message": "invalid phone number"})

    if not type(customer.birth_date) == date or type(customer.birth_date) == str:
        try:
            customer.birth_date = datetime.strptime(customer.birth_date, "%Y-%m-%d").date()
        except:
            errors.append({"field": "birth_date", "message": "invalid birth date"})

    return errors



def timing_validator(timing):
    errors = []
    if not type(timing.date) == date or type(timing.date) == str:
        try:
            timing.date = datetime.strptime(timing.date, "%Y-%m-%d").date()
        except:
            errors.append({"field": "date", "message": "invalid date"})

    if not type(timing.start_time) == str or not re.match(r"^\d{2}:\d{2}$", timing.start_time):
        errors.append({"field": "start_time", "message": "invalid start time"})

    if not type(timing.end_time) == str or not re.match(r"^\d{2}:\d{2}$", timing.end_time):
        errors.append({"field": "end_time", "message": "invalid end time"})

    if timing.start_time >= timing.end_time:
        errors.append({"field": "time", "message": "end time must be after start time"})

    if not timing.status in ["available", "booked"]:
        errors.append({"field": "status", "message": "invalid status"})

    return errors



def visit_validator(visit):
    errors = []
    if not type(visit.reason) == str or len(visit.reason) < 3:
        errors.append({"field": "reason", "message": "invalid reason"})

    if not type(visit.fee) == int or visit.fee < 0:
        errors.append({"field": "fee", "message": "invalid fee"})

    if not visit.visit_status in ["Pending", "Completed", "Cancelled"]:
        errors.append({"field": "visit_status", "message": "invalid visit status"})

    if not type(visit.customer_id) == int:
        errors.append({"field": "customer_id", "message": "invalid customer ID"})

    if not type(visit.schedule_id) == int:
        errors.append({"field": "schedule_id", "message": "invalid schedule ID"})

    return errors
