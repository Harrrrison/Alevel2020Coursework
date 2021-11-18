import sqlite3


DB_NAME = "UsersDataBase.db"
SALT = "MJS12345433"


def get_database_connection():
    con = sqlite3.connect(DB_NAME)
    return con


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")


def create_database(connection):
    try:
        file = open("Schema.sql")
        query = file.read()
        connection.executescript(query)
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")


def print_tables(connection):
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = execute_query(connection, query)
    tables_list = []
    for item in tables:
        tables_list.append(item[0])
    print(tables_list)

if __name__ == '__main__':
    print(".")