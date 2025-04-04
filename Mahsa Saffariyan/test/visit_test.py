from datetime import date

from controller.visit_controller import VisitController
from model.visit import Visit
from repository.visit_repository import VisitRepository
from validation.validator import visit_validator

visit_controller = VisitController()
print(visit_controller.save(1, 1, "Routine Checkup", 100, "Pending"))

# repo = VisitRepository()
# visit = Visit(1, 1, 1, 'Routine Checkup', 100, 'Pending')

# Test Passed
# repo.save(visit)

# Test Passed
# print(visit_validator(visit))
# repo.edit(visit)

# Test Passed
# repo.remove(1)

# Test Passed
# print(repo.find_all())

# Test Passed
# print(repo.find_by_id(1))
