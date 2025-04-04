class Customer:
    def __init__(self, customer_id, first_name, family_name, gender, phone, birth_date, medical_history=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.family_name = family_name
        self.gender = gender
        self.phone = phone
        self.birth_date = birth_date
        self.medical_history = medical_history

    def __repr__(self):
        return f"{self.__dict__}"
