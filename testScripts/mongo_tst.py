# from pymongo import MongoClient
# client = MongoClient('mongodb://localhost:27017')
# db = client['test']
# customer = db.CustomerMaster
# #CustomerMasterData = customer.find({"externalSourceInfo.externalSourceCreatedby" : {'$in':['dataMigration','cmarco','cacarsystem','datateam','cacargroup.macro03','roPush','lhaven','kathryn.hatcher','jessica','bmangabay','agregory','mtroche','dean','daphneb','gmossprod','christopherg','justinh','bhumphrey','jduncan','cmacro15','fbarsamela','lfranklin','grnrub222','gracef','mhkrishna','cadadmin','Data Migration','anand','datamigration','DataMirgration','','DataMigration','brieanav','mike']}})
# CustomerMasterData = client.list_database_names()




from json import load
import subprocess
import ast

mongo_preprod_db_config = dict()
mongo_preprod_db_config["rsnew1"] = {
    "username": "srajendran_pre",
    "password": "u9suT9eIbq2fh7KC",
    "host": "rsnew1/172.31.255.99:27017,172.31.203.137:27017,172.31.169.125:27017"
}
mongo_preprod_db_config["rsnew2"] = {
    "username": "srajendran_pre",
    "password": "u9suT9eIbq2fh7KC",
    "host": "rsnew2/172.31.141.190:27017,172.31.189.100:27017,172.31.134.113:27017"
}

get_all_dbname_query_statement = dict({"mongo": "db.getMongo().getDBNames()", "mysql": """ "select schema_name from information_schema.schemata where schema_name like 'dealer_accounting_%'" """})

mysql_preprod_db_config = dict()
mysql_preprod_db_config["accounting"] = {
    "usename": "srajendran_pre",
    "password": "u9suT9eIbq2fh7KC",
    "host": "tkpreprod-arc-accounting-0-reader.cpjhw84zugns.us-west-1.rds.amazonaws.com"
}


# print(mongo_preprod_db_config.get("rsnew1")['username'])

def load_all_dbs_from_mongo():
    preprod_mongo_dbs = list()
    tmp_db_list = list()
    for instance_key, instance_details in mongo_preprod_db_config.items():
        print(instance_key)
        mongo_get_db = f"sudo mongo --authenticationDatabase admin --host '{instance_details['host']}' --username '{instance_details['username']}' --password {instance_details['password']} --eval '{get_all_dbname_query_statement['mongo']}' |sed -n -e '/MongoDB server*/,//p' |egrep -v '(CONNPOOL|WARNING|server)'"
        mongo_results = subprocess.run(mongo_get_db,shell=True, stdout=subprocess.PIPE)
        mongo_all_dbs = ast.literal_eval(mongo_results.stdout.decode())
        tmp_db_list.append(mongo_all_dbs)
    preprod_mongo_dbs = tmp_db_list
    return preprod_mongo_dbs

print(len(load_all_dbs_from_mongo()))





def load_all_dbs_from_mysql():
    _tmp_db_list = list()
    for instance_key, instance_details in mysql_preprod_db_config.items():
        mysql_get_db_cmd = f"sudo mysql -u {instance_details['usename']} -p'{instance_details['password']}' -h '{instance_details['host']}' -e {get_all_dbname_query_statement['mysql']}"
        mysql_results = subprocess.run(mysql_get_db_cmd, shell=True, stdout=subprocess.PIPE)
        mysql_acc_dbs = mysql_results.stdout.decode().split("\n")
        _tmp_db_list.append(mysql_acc_dbs)
    preprod_acc_dbs = _tmp_db_list
    return preprod_acc_dbs
    
print(load_all_dbs_from_mysql())