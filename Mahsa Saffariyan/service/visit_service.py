from repository.visit_repository import VisitRepository
from model.visit import Visit


class VisitService:
    def __init__(self):
        self.repo = VisitRepository()

    def book_visit(self, visit):
        self.repo.book_visit(visit)

    def complete_visit(self, visit_id):
        self.repo.complete_visit(visit_id)

    def remove(self, visit_id):
        self.repo.remove(visit_id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_customer_id(self, customer_id):
        return self.repo.find_by_customer_id(customer_id)

    def find_pending_visits(self):
        return self.repo.find_pending_visits()

    def find_pending_by_customer_id(self, customer_id):
        return self.repo.find_pending_by_customer_id(customer_id)
