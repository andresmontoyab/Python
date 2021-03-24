import pymongo

# Steps to install mongo in Mac
# 1. brew tap mongodb/brew
# 2. brew install mongodb-community@4.4
# 3. brew services start mongodb-community@4.4
# 4. mongo -> Enter to mongo db
# 5. show dbs -> Muestra las dbs
# 6. use PythonCourse -> Create db that is called PythonCourse

class NoSql():

    def __init__(self):
        conn = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        database = conn["PythonCourse"]
        databases = conn.list_database_names()
        self.__retrieve_collection(database)
        self.__insert_document(database)
        self.__insert_multiple_documents(database)
        self.__find_information(database)
        self.__query_data(database)
        self.__update_documents(database)
        self.__delete_documents(database)

    def __retrieve_collection(self, database):
        print("Creating Collection")
        collections = database.list_collection_names()
        print(collections)

    def __insert_document(self, database):
        print("Inserting elements")
        collection = database['user']
        insert= {"name":"Salome", "age": "22"}
        result = collection.insert_one(insert)
        print(result)

    def __insert_multiple_documents(self, database):
        print("")
        collection = database['user']
        insert = {"name": "Salome", "age": "22"}
        insert_two = {"name": "Ben", "age": "25 "}
        insert_three = {"name": "Emma", "age": "27 "}
        result = collection.insert_many([insert, insert_two, insert_three])
        print(result.inserted_ids)

    def __find_information(self, database):
        print("Find Info From DB")
        collection = database['user']
        find = collection.find_one()
        print(find)
        for find in collection.find():
            print(find)

    def __query_data(self, database):
        print("Query Data From DB")
        collection = database['user']
        query = {"name":"Ben"}
        documents = collection.find(query)
        for find in documents:
            print(find)

    def __update_documents(self, database):
        print("Updating Records")
        collection = database['user']
        query = {"name": "Salome"}
        new_name = {"$set": {"name": "Alexaaaa Davvvvv"}}
        collection.update_one(query, new_name)
        for i in collection.find():
            print(i)



    def __delete_documents(self, database):
        print("Delete Documents Records")
        collection = database['user']
        query = {"name": "Salome"}
        collection.delete_many(query)
        for i in collection.find():
            print(i)

no_sql = NoSql()
