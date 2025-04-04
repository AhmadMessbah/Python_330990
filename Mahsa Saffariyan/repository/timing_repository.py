import mysql.connector
from model.timing import Timing

class TimingRepository:
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

    def save(self, timing):
        self.connect()
        self.cursor.execute(
            "INSERT INTO TIMINGS (DATE, START_TIME, END_TIME, STATUS, DOCTOR_NAME) VALUES (%s, %s, %s, %s, %s)",
            [timing.date, timing.start_time, timing.end_time, timing.status, timing.doctor_name]
        )
        self.connection.commit()
        self.disconnect()

    def edit(self, timing):
        self.connect()
        self.cursor.execute(
            "UPDATE TIMINGS SET DATE=%s, START_TIME=%s, END_TIME=%s, STATUS=%s, DOCTOR_NAME=%s WHERE SCHEDULE_ID=%s",
            [timing.date, timing.start_time, timing.end_time, timing.status, timing.doctor_name, timing.schedule_id]
        )
        self.connection.commit()
        self.disconnect()

    def remove(self, schedule_id):
        self.connect()
        self.cursor.execute("DELETE FROM TIMINGS WHERE SCHEDULE_ID=%s", [schedule_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM TIMINGS ORDER BY DATE, START_TIME")
        timings = list(map(lambda t: Timing(*t), self.cursor.fetchall()))
        self.disconnect()
        return timings

    def find_by_id(self, schedule_id):
        self.connect()
        self.cursor.execute("SELECT * FROM TIMINGS WHERE SCHEDULE_ID=%s", [schedule_id])
        timing = self.cursor.fetchone()
        self.disconnect()
        return Timing(*timing) if timing else None

