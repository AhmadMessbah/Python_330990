from model.timing import Timing
from service.timing_service import TimingService
from validation.validator import timing_validator


def error_handler(my_function):
    def inner(*args, **kwargs):
        try:
            result = my_function(*args, **kwargs)
            return True, result
        except Exception as e:
            return False, e

    return inner


class TimingController:
    def __init__(self):
        self.service = TimingService()

    @error_handler
    def save(self, date, start_time, end_time, status, doctor_name):
        timing = Timing(None, date, start_time, end_time, status, doctor_name)
        errors = timing_validator(timing)
        if errors:
            raise Exception(errors)
        self.service.save(timing)
        return "Timing Saved"

    @error_handler
    def edit(self, schedule_id, date, start_time, end_time, status, doctor_name):
        timing = Timing(schedule_id, date, start_time, end_time, status, doctor_name)
        errors = timing_validator(timing)
        if errors:
            raise Exception(errors)
        self.service.edit(timing)
        return "Timing Edited"

    @error_handler
    def remove(self, schedule_id):
        self.service.remove(schedule_id)
        return "Timing Removed"

    @error_handler
    def find_all(self):
        return self.service.find_all()
