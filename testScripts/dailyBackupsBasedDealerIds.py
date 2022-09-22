import dbs

from tqdm import tqdm

def getObjDBS(preprod_databases: list):
    for dbs in preprod_databases:
        yield dbs

def getEnvName(dbs_src_args: list):
    key_name = [env_key for env_key in dbs_src_args]
    key_name = "".join(key_name)
    return key_name

def checking_parsed_dealer_is_list_or_not(given_list):
    if(type(given_list) == list):
        return True
    else:
        print("ISSUE WITH GIVEN LIST")
        return False

def getDatabasesWithTodayDealerIds(preprod_dbs_list: dict, today_dealer_ids: list):
    foundedTenants = []
    dbList_key_name = preprod_dbs_list.keys()
    key_name = getEnvName(dbList_key_name)
    if(checking_parsed_dealer_is_list_or_not(today_dealer_ids) and True):
        for dbs in getObjDBS(preprod_dbs_list.get(key_name)):
            for dealer in dbs:
                for dealer_id in today_dealer_ids:
                    if(dealer.endswith(dealer_id)):
                        foundedTenants.append(dealer)
    else:
        print(
            "Kindly provide the dealer ids with py-list format like ['121', '122']!")
    filtered_with_today_dealerIds = set(foundedTenants)
    filtered_with_today_dealerIds = list(filtered_with_today_dealerIds)
    return filtered_with_today_dealerIds

def getSeggregate_arc_crm(filtered_dealer_dbs: list):
    arc_dbs = []
    crm_dbs = []
    for db in filtered_dealer_dbs:
        tmp_tenant_name = db.split("_")[1]
        tmp_crm_tenant_name = db.split("_")[2]
        if(tmp_tenant_name != 'crm'):
            arc_dbs.append(db)
            arc_tenant_db = "tenant_" + tmp_tenant_name
            if arc_tenant_db not in [arc_db for arc_db in arc_dbs]:
                arc_dbs.append(arc_tenant_db)
        else:
            crm_dbs.append(db)
            crm_tenant_db = "crm_tenant_" + tmp_crm_tenant_name
            if crm_tenant_db not in [crmdb for crmdb in crm_dbs]:
                crm_dbs.append(crm_tenant_db)
    return {"arc_dbs": arc_dbs, "crm_dbs": crm_dbs}


def main():
    preprod_mongo_dbs = [dbs.rsnew1_dbs,
                         dbs.rsnew2_dbs]
    accounting_dbs = [dbs.accounting_dbs]
    today_dealer_ids = ["1482", "1481", "1476", "1117", "1118", "1198",
                        "1199", "1234", "1223", "1497", "1110", "1223", "1480", "1479"]
    if checking_parsed_dealer_is_list_or_not(today_dealer_ids):
        # printing arc and crm dbs, passing to anothe
        # r function since we seggregating those.
        dealer_arc_crm_dbs_list = getSeggregate_arc_crm(getDatabasesWithTodayDealerIds(
            {"mongo_preprod_arc_crm": preprod_mongo_dbs}, today_dealer_ids))
        print('\n')
        print('Mongo(DMS & CRM) and  MySQL(DMS & parts),')
        for dealer_type, dealer_dbs in dealer_arc_crm_dbs_list.items():
            print(dealer_type, ": \n")
            dealer_dbs.sort()
            for dealer_db in dealer_dbs:
                print(dealer_db)
            print('\n')

        # printing accounting dbs
        dealer_arc_accounting_dbs_list = getDatabasesWithTodayDealerIds(
            {"mysql_preprod_acc_dbs": accounting_dbs},
            today_dealer_ids
        )
        print('\n')
        print('MySQL Accounting, \n')
        dealer_arc_accounting_dbs_list.sort()
        for acc_db in dealer_arc_accounting_dbs_list:
            print(acc_db, end='\n')
    else:
        print("Error: Please check the given dealer list!")
        print('\n')


if __name__ == "__main__":
    main()

# # ["1483", "1207", "1102", "1474", "1208", "1435", "947", "953","852", "853","35001", "35002",
    # "905", "1151", "1150", "1474",  "1464", "1222", "1224"]
# >>> import subprocess
# >>> rsnew2_cmd="sudo mongo --host 'rsnew2/172.31.141.190:27017,172.31.189.100:27017,172.31.134.113:27017' --authenticationDatabase 'admin' --username 'srajendran_pre' --password 'u9suT9eIbq2fh7KC' --eval 'db.getMongo().getDBNames()'|sed -n -e '/MongoDB server*/,//p' |egrep -v '(CONNPOOL|WARNING|server)'"
# >>> rsnew2_results = subprocess.run(rsnew2_cmd,shell=True, stdout=subprocess.PIPE)
# >>> rsnew2_dbs = ast.literal_eval(rsnew2_results.stdout.decode())
# >>> len(rsnew2_dbs)
# 577
