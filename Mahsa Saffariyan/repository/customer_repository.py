import mysql.connector
from model.customer import Customer

class CustomerRepository:
    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root123",
            database="appointment_system"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, customer):
        self.connect()
        self.cursor.execute(
            "INSERT INTO CUSTOMERS (FIRST_NAME, FAMILY_NAME, GENDER, PHONE, BIRTH_DATE) VALUES (%s, %s, %s, %s, %s)",
            [customer.first_name, customer.family_name, customer.gender, customer.phone, customer.birth_date]
        )
        self.connection.commit()
        self.disconnect()

    def edit(self, customer):
        self.connect()
        self.cursor.execute(
            "UPDATE CUSTOMERS SET FIRST_NAME=%s, FAMILY_NAME=%s, GENDER=%s, PHONE=%s, BIRTH_DATE=%s WHERE CUSTOMER_ID=%s",
            [customer.first_name, customer.family_name, customer.gender, customer.phone, customer.birth_date, customer.customer_id]
        )
        self.connection.commit()
        self.disconnect()

    def remove(self, customer_id):
        self.connect()
        self.cursor.execute("DELETE FROM CUSTOMERS WHERE CUSTOMER_ID=%s", [customer_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM CUSTOMERS ORDER BY FAMILY_NAME, FIRST_NAME")
        customers = list(map(lambda c: Customer(*c), self.cursor.fetchall()))
        self.disconnect()
        return customers

    def find_by_id(self, customer_id):
        self.connect()
        self.cursor.execute("SELECT * FROM CUSTOMERS WHERE CUSTOMER_ID=%s", [customer_id])
        customer = self.cursor.fetchone()
        self.disconnect()
        return Customer(*customer) if customer else None

    def find_by_name_and_family(self, first_name, family_name):
        self.connect()
        self.cursor.execute(
            "SELECT * FROM CUSTOMERS WHERE FIRST_NAME LIKE %s AND FAMILY_NAME LIKE %s",
            [first_name + "%", family_name + "%"]
        )
        customers = list(map(lambda c: Customer(*c), self.cursor.fetchall()))
        self.disconnect()
        return customers

