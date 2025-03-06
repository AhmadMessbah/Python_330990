import mysql.connector
from model.person import Person


class PersonRepository:
    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root1234",
            database="patient_db"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, person):
        self.connect()
        self.cursor.execute(
            "INSERT INTO PERSONS (NAME,FAMILY,BIRTH_DATE,USERNAME,PASSWORD) VALUES (%s,%s,%s,%s,%s)",
            [person.name, person.family, person.birth_date, person.username, person.password]
        )
        self.connection.commit()
        self.disconnect()

    def edit(self, person):
        self.connect()
        self.cursor.execute(
            "UPDATE PERSONS SET NAME=%s, FAMILY=%s, BIRTH_DATE=%s, USERNAME=%s,PASSWORD=%s WHERE P_ID=%s",
            [person.name, person.family, person.birth_date, person.username, person.password, person.id]
        )
        self.connection.commit()
        self.disconnect()

    def remove(self, person_id):
        self.connect()
        self.cursor.execute("DELETE FROM PERSONS WHERE P_ID=%s", [person_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM PERSONS ORDER BY FAMILY, NAME")
        person_list = list(map( lambda p:Person(p[0],p[1],p[2],str(p[3]),p[4],p[5],) , self.cursor.fetchall()))
        self.disconnect()
        return person_list

    def find_by_id(self, person_id):
        self.connect()
        self.cursor.execute("SELECT * FROM PERSONS WHERE P_ID=%s", [person_id])
        person = self.cursor.fetchone()
        self.disconnect()
        return person

    def find_by_name_and_family(self, name, family):
        self.connect()
        self.cursor.execute("SELECT * FROM PERSONS WHERE NAME LIKE %s AND FAMILY LIKE %s", [name + "%", family + "%"])
        person_list = self.cursor.fetchall()
        self.disconnect()
        return person_list

    def find_by_username_and_password(self, username, password):
        self.connect()
        self.cursor.execute("SELECT * FROM PERSONS WHERE USERNAME=%s AND PASSWORD=%s", [username, password])
        person = self.cursor.fetchone()
        self.disconnect()
        return person
