import mysql.connector  

def get_db_connection():
    return mysql.connector.connect(
        host="34.46.25.191",
        user="avayainfinitydb",
        password="Avaya123",
        database="infinitybankdb",
        port=3306
    )
