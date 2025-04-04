from datetime import date

from controller.timing_controller import TimingController
from model.timing import Timing
from repository.timing_repository import TimingRepository
from validation.validator import timing_validator

timing_controller = TimingController()
print(timing_controller.save(date(2025, 4, 5), "09:00", "10:00", "available", "Dr. Smith"))

# repo = TimingRepository()
# timing = Timing(1, '2025-04-05', '09:00', '10:00', 'available', 'Dr. Smith')

# Test Passed
# repo.save(timing)

# Test Passed
# print(timing_validator(timing))
# repo.edit(timing)

# Test Passed
# repo.remove(1)

# Test Passed
# print(repo.find_all())

# Test Passed
# print(repo.find_by_id(1))
