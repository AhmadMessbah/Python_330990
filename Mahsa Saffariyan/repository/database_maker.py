import mysql.connector

def create_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123"
    )
    cursor = connection.cursor()
    with open("repository/database.sql") as f:
        for sql_command in f.read().split("--"):
            if sql_command.strip():
                print(sql_command.strip())
                cursor.execute(sql_command.strip())
    connection.commit()
    cursor.close()
    connection.close()
