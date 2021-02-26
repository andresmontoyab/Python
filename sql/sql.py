import sqlite3




class SQL:


    def main(self):
        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            print("Connected ")
            self.creatin_a_table(conn)
        except sqlite3.Error as error:
            print ("Process Fails To connected")
        finally:
            cursor.close()
            print("Closing Connection")

    def creatin_a_table(self, conn):
        conn.execute('''CREATE TABLE STD(stdid INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT(20) NOT NULL, age INTEGER, dept TEXT(20));''')


sql = SQL()
sql.main()