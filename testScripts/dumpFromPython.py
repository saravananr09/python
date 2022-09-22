import bson
from pymongo import MongoClient
import os



def dump(collections, conn, db_name, path):
    db = conn[db_name]
    for coll in collections:
        with open(os.path.join(path, f'{coll}.bson'), 'wb+') as f:
            for doc in db[coll].find():
                f.write(bson.BSON.encode(doc))


def restore(path, conn, db_name):
    # conn = MongoClient("mongodb://admin:admin@127.0.0.1:27017", authSource="admin")
    # db_name = 'my_db'
    # restore(DB_BACKUP_DIR, conn, db_name)
    db = conn[db_name]
    for coll in os.listdir(path):
        if coll.endswith('.bson'):
            with open(os.path.join(path, coll), 'rb+') as f:
                db[coll.split('.')[0]].insert_many(bson.decode_all(f.read()))


DB_BACKUP_DIR = '/Users/saravanan/python/testScripts/test_bkups/'
source_conn = MongoClient("mongodb://root:root@localhost:27017", authSource="admin")
sourcedb_name = 'm201'
collections = ['test']
dump(collections, source_conn, sourcedb_name, DB_BACKUP_DIR)


dest_conn = MongoClient("mongodb://root:root@localhost:27017", authSource="admin")
destdb_name = 'testing'
collections = ['test']
restore(DB_BACKUP_DIR,dest_conn, destdb_name)






