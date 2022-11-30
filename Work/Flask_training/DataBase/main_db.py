import sqlite3

# conn = sqlite3.connect("panda.db")
# cur = conn.cursor()

class flask_user:

    def __init__(self, db_Input_name):
      self.dbName = db_Input_name

    def CheckRegistr(self, login, verification=False):
        try:
            conn = sqlite3.connect(self.dbName, check_same_thread=False)
            cursor = conn.cursor()

            with conn:
                if verification == False:
                    login_result = cursor.execute("SELECT * FROM 'users' WHERE login = ?", (login,)).fetchall()
                    return bool(len(login_result))
                else:
                    password_data = cursor.execute("SELECT password FROM 'users' WHERE login = ?", (login,)).fetchone()
                    password_verification = password_data[0]
                    verification = False
                    return password_verification

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if conn:
                conn.close()
                print("Conn close")
    
    def AddUser(self, login, password, email, phone_number):
        try:
            conn = sqlite3.connect(self.dbName, check_same_thread=False)
            cursor = conn.cursor()

            with conn:
                return cursor.execute("INSERT INTO 'users' ('login', 'password', 'email', 'phone_number') VALUES (?, ?, ?, ?)", (login, password, email, phone_number,))

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if conn:
                conn.close()
                print("Conn close")

    def GettingData_Items(self):
        try:
            conn = sqlite3.connect(self.dbName, check_same_thread=False)
            cursor = conn.cursor()

            with conn:
                cursor.execute("SELECT * FROM 'items'")
            return cursor.fetchall()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if conn:
                conn.close()
                print("Conn close")

