import pymongo

DB_IP = "9.30.251.243"
DB_PORT = "27017"
DB_USERNAME = "admin"
DB_PASS = "admin"
DATABASE = "my_notes"
COLLECTION_NAME = "dummy_notes"


def connect_mongo():
    myclient = pymongo.MongoClient("mongodb://" + DB_USERNAME + ":" + DB_PASS + "@" + DB_IP + ":" + DB_PORT)
    return myclient


def fetch_data():
    result_data = []
    my_client = connect_mongo()
    db_obj = my_client[DATABASE]
    collection_obj = db_obj[COLLECTION_NAME]
    for item in collection_obj.find():
        result_data.append(item)

    return result_data


def insert_data(data):
    my_client = connect_mongo()
    db_obj = my_client[DATABASE]
    collection_obj = db_obj[COLLECTION_NAME]
    insert_status = collection_obj.insert_one(data)
    if insert_status:
        return "data inserted"
    else:
        return "failed to insert data"

