import sqlite3

DB_NAME = "UsersDataBase.db"
SALT = "MJS12345433"


def get_database_connection():
    con = sqlite3.connect(DB_NAME)
    return con


def test_execute(connection, query):
    cursor = connection.cursor()
    for row in cursor.execute(query):
        print(row)
        return True


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
        return cursor.fetchone()
    except sqlite3.Error as e:
        if e == 'UNIQUE constraint failed: users.email':
            print("Email not unique")
            return False
        else:
            print(f"The error '{e}' occurred")
            return False


def execute_select_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    return execute_query(connection, query)


def create_database(connection):
    try:
        # r"C:\Users\ruthr\PycharmProjects\Alevel2020Coursework\
        # Windows version
        try:
            # file = open(r"C:\Users\ruthr\PycharmProjects\Alevel2020Coursework\Schema")
            file = open(r'/Users/harrisonrigby/PycharmProjects/Alevel2020_Coursework/Schema')
        except FileNotFoundError:
            file = open("Schema")
            print("file not found")

        query = file.read()
        connection.executescript(query)
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")


def username_validation(connection, username):
    query = f"SELECT email FROM users WHERE username == ('{username}') ;"
    tables = execute_query(connection, query)
    tables_list = []
    try:
        for item in tables:
            tables_list.append(item)
        print(tables_list)
        print("invalid username")
        return True
    except:
        print("valid username")
        return False


def email_validation(connection, email):
    query = f"SELECT username FROM users WHERE email == ('{email}') ;"
    tables = execute_query(connection, query)
    tables_list = []
    try:
        for item in tables:
            tables_list.append(item[0])
        print(tables_list)
        print("valid email")
        return True
    except:
        print("invalid email")
        return False

def validation(connection, query):
    tables = execute_query(connection, query)
    tables_list = []
    try:
        for item in tables:
            tables_list.append(item[0])
        print(tables_list)
        return True
    except:
        return False


if __name__ == '__main__':
    print(".")
    username_validation(get_database_connection(), 'Harrison')
    create_database(get_database_connection())
