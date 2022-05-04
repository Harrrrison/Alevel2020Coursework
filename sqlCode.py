import sqlite3

DB_NAME = "UsersDataBase.db"
SALT = "MJS12345433"


def get_database_connection(): # a Connection to the database has to be established before any query is executed
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
        cursor.execute(query) # gets the query as a paramiter then executes it from the connection
        connection.commit()
        print("Query executed successfully")
        return cursor.fetchone()
    except sqlite3.Error as e:
        if e == 'UNIQUE constraint failed: users.email':
            print("Email not unique")
            return False
        else:
            print(f"The error '{e}' occurred") # SQL doesnt print console errors hence the self error printing
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
            file = open(r'/Users/harrisonrigby/PycharmProjects/Alevel2020_Coursework/Schema') # the schemea needs to
            # be opened for the database to be creaetd
        except FileNotFoundError:
            file = open("Schema")
            print("file not found")

        query = file.read()
        connection.executescript(query)
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")


def username_validation(connection, username):
    # will take the inputted username and check if there is a email associated to validata it is in the database
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
    # will take the user email and check if there is a username associated to validata it is in the database
    query = f"SELECT username FROM users WHERE email == ('{email}') ;"
    tables = execute_query(connection, query)
    tables_list = []
    try:
        for item in tables:
            tables_list.append(item)
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


def username_and_password_validation(connection, username, hashedPassword):
    # will take the username and a hashed password and compares the hashed password in the database to the hashed
    # password taken in to authroise the user
    query = f"SELECT password FROM users WHERE username == ('{username}') ;"
    tables = execute_query(connection, query)
    tables_list = []
    try:
        print(tables_list)
        for item in tables:
            tables_list.append(item)
        if hashedPassword == item:
            return True
        else:
            print("username not matching password")
            return False
    except:
        print("username not in system")
        return False


if __name__ == '__main__':
    print(".")
    email_validation(get_database_connection(), 'harrisonrigby@icloud.com')
    create_database(get_database_connection())
