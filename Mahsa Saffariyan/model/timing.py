class Timing:
    def __init__(self, schedule_id, date, start_time, end_time, status, doctor_name):
        self.schedule_id = schedule_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.doctor_name = doctor_name

    def __repr__(self):
        return f"{self.__dict__}"
