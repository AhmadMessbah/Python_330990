import re
from datetime import date, datetime

from model.person import Person


def person_validator(person):
    errors = []
    if not type(person.name) == str or not re.match(r"^[a-zA-Z\s]{3,30}$", person.name):
        errors.append({"field": "name", "message": "invalid name"})

    if not type(person.family)== str or not re.match(r"^[a-zA-Z\s]{3,30}$", person.family):
        errors.append({"field": "family", "message": "invalid family"})

    # todo : has error
    # if not type(person.birth_date) == date or type(person.birth_date) == str:
    #     try:
    #         person.birth_date = datetime.strptime(person.birth_date, "%Y-%m-%d")
    #     except:
    #         errors.append({"field": "birth_date", "message": "invalid birth date"})
    # else:
    #     errors.append({"field": "birth_date", "message": "invalid birth_date"})
    return errors

