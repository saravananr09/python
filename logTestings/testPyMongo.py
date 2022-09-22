from pymongo import MongoClient

# mongodb+srv://saravanan:<password>@kumbcluster.l6whs.mongodb.net/test
client = MongoClient("mongodb+srv://saravanan:BFK8zXdhUBvZ3FFN@kumbcluster.l6whs.mongodb.net/kumbCluster")

def getDbs():
    for dbs in client.list_databases():
        for key, db in dbs.items():
            if key == 'name':
                yield db

mongodbs = getDbs()


def getCollectioWithDb():
    for db in mongodbs:
        if db in ['admin', 'local']:
            continue
        print(f"Collections from the {db}")
        getColl = client[db]
        for coll in getColl.list_collection_names():
            print(coll)
        
# getCollectioWithDb()








# to trigger simple find command

# myDb = client['sample_analytics']
# coll = myDb.kumb

# for coll in myDb.list_collection_names():
#     print(coll)

# simpleFind = coll.find({'name': 'saravananr'})
# for i in simpleFind:
#     print(i)


