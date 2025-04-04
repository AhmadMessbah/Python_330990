from model.visit import Visit
from service.visit_service import VisitService
from validation.validator import visit_validator


def error_handler(my_function):
    def inner(*args, **kwargs):
        try:
            result = my_function(*args, **kwargs)
            return True, result
        except Exception as e:
            return False, e

    return inner


class VisitController:
    def __init__(self):
        self.service = VisitService()

    @error_handler
    def book_visit(self, customer_id, schedule_id, reason, fee, visit_status):
        visit = Visit(None, customer_id, schedule_id, reason, fee, visit_status)
        errors = visit_validator(visit)
        if errors:
            raise Exception(errors)
        self.service.book_visit(visit)
        return "Visit Booked"

    @error_handler
    def complete_visit(self, visit_id):
        self.service.complete_visit(visit_id)
        return "Visit Completed"

    @error_handler
    def remove(self, visit_id):
        self.service.remove(visit_id)
        return "Visit Removed"

    @error_handler
    def find_all(self):
        return self.service.find_all()
