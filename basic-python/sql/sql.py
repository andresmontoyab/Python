import sqlite3

class SQL:
    def main(self):
        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            print("Connected ")
            #self.creating_a_table(conn)
            self.insert_data(cursor)
            self.retrieve_data(cursor)
            self.update_data(cursor)
            self.delete_data(cursor)
            conn.commit()
        except sqlite3.Error as error:
            print ("Process Fails To connected")
        finally:
            cursor.close()
            print("Closing Connection")

    def creating_a_table(self, conn):
        conn.execute('''CREATE TABLE STD(stdid INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT(20) NOT NULL, age INTEGER, dept TEXT(20));''')

    def insert_data(self, cursor):
        query = "INSERT INTO STD(name,age,dept) values ('andres',20,'CS');"
        try:
            cursor.execute(query)
            print("Everything goes good, data inserted")
        except:
            print("Error in Database")

    def retrieve_data(self, cursor):
        select = "SELECT * FROM STD;"
        cursor.execute(select)
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            print(record)

    def update_data(self, cursor):
        query = "UPDATE STD set age = 25 WHERE stdid = 2;"
        try:
            cursor.execute(query)
            print("Updation was good")
        except:
            print("Something was wrong")

    def delete_data(self, cursor):
        query = "DELETE FROM STD WHERE stdid = 5;"
        try:
            cursor.execute(query)
            print("Deletion was good")
        except:
            print("Something was wrong with the deletion")



sql = SQL()
sql.main()