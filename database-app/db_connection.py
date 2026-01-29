import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Update if your root user has a password
        database="gameappdb",
        port=3306
    )
