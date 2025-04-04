import mysql.connector
from datetime import date
from model.visit import Visit
from model.customer import Customer
from model.timing import Timing

class VisitRepository:
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

    def convert_visit_tuple_to_object(self, visit_tuple):
        customer = Customer(*visit_tuple[6:12])
        timing = Timing(*visit_tuple[12:])
        return Visit(*visit_tuple[:6], customer, timing)

    def book_visit(self, visit):
        self.connect()
        self.cursor.execute("INSERT INTO VISITS (CUSTOMER_ID, SCHEDULE_ID, REASON, FEE, VISIT_STATUS) VALUES (%s, %s, %s, %s, %s)",
                            [visit.customer_id, visit.schedule_id, visit.reason, visit.fee, visit.visit_status])
        self.connection.commit()
        self.disconnect()

    def complete_visit(self, visit_id):
        self.connect()
        self.cursor.execute("UPDATE VISITS SET VISIT_STATUS=%s WHERE VISIT_ID=%s",
                            ["Completed", visit_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM VISIT_REPORT")
        visits = list(map(self.convert_visit_tuple_to_object, self.cursor.fetchall()))
        self.disconnect()
        return visits

    def find_by_customer_id(self, customer_id):
        self.connect()
        self.cursor.execute("SELECT * FROM VISITS WHERE CUSTOMER_ID=%s", [customer_id])
        visits = list(map(self.convert_visit_tuple_to_object, self.cursor.fetchall()))
        self.disconnect()
        return visits

    def find_pending_visits(self):
        self.connect()
        self.cursor.execute("SELECT * FROM VISITS WHERE VISIT_STATUS=%s", ["Pending"])
        visits = list(map(self.convert_visit_tuple_to_object, self.cursor.fetchall()))
        self.disconnect()
        return visits

