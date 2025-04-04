class Visit:
    def __init__(self, visit_id, customer_id, schedule_id, reason, fee=0, visit_status="Pending"):
        self.visit_id = visit_id
        self.customer_id = customer_id
        self.schedule_id = schedule_id
        self.reason = reason
        self.fee = fee
        self.visit_status = visit_status

    def __repr__(self):
        return f"{self.__dict__}"



