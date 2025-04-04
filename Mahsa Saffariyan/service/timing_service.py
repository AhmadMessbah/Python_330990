from repository.timing_repository import TimingRepository
from model.timing import Timing


class TimingService:
    def __init__(self):
        self.repo = TimingRepository()

    def save(self, timing):
        self.repo.save(timing)

    def edit(self, timing):
        self.repo.edit(timing)

    def remove(self, schedule_id):
        self.repo.remove(schedule_id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self, schedule_id):
        return self.repo.find_by_id(schedule_id)
