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
        # r"C:\Users\ruthr\PycharmProjects\Alevel2020Coursework\
        #Windows version
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

'''
def print_tables(connection):
    query = f"SELECT email FROM sqlite_master WHERE type='table';"
    tables = execute_query(connection, query)
    tables_list = []
    for item in tables:
        tables_list.append(item[0])
    print(tables_list)
'''

if __name__ == '__main__':
    print(".")
    create_database(get_database_connection())