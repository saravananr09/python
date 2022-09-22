
list = [0,1,2,3,4,5,6,7,8,9,10]
from tabnanny import check
import dbs
# for i in range(len(list),0,-1):
# 	i = i - 1
# 	if (i <= 6 and i >= 2):
# 		print()
# 		#print("list is ", list[i])



# for y in range(-(len(list)), 0,1):
# 	i = i - 1
# 	print(i, list[y])


# accounting_dbs = dbs.accounting_dbs

# def getEnvName(dealer_dbs_src: dict):
#     mongo_key_name = "".join([env_key for env_key in dealer_dbs_src.keys() if env_key == 'preprod_acc_dbs'])
#     return mongo_key_name

# print(getEnvName({"preprod_acc_dbs": accounting_dbs}))


# taken = ["dealer_bayouautogroup_1481", "dealer_bayouautogroup_1482", "tenant_bayouautogroup", "dealer_anthonyautogroup_1476", "tenant_anthonyautogroup", "dealer_dselite_tauranfoley_114", "dealer_houseofcars_1199", "dealer_houseofcars_1208", "tenant_houseofcars", "dealer_ewingautogroup_1103", "dealer_ewingautogroup_1102", "tenant_ewingautogroup", "dealer_communityautomotive_1471", "tenant_communityautomotive", "dealer_mossmotors_1109", "tenant_mossmotors", "dealer_kengarffautomotive_1473", "tenant_kengarffautomotive", "dealer_keyesmotors_1114", "tenant_keyesmotors", "dealer_beckmotors_1483", "tenant_beckmotors", "dealer_ewingautogroup_1435", "tenant_ewingautogroup", "dealer_crm_tauranfoley_114", "crm_tenant_tauranfoley", "dealer_crm_smpgroup_1193", "crm_tenant_smpgroup", "dealer_accounting_bayouautogroup_1481", "dealer_accounting_bayouautogroup_1482", "dealer_accounting_tekiondeal_114", "dealer_accounting_ewingautogroup_1103", "dealer_accounting_communityautomotive_1471", "dealer_accounting_ewingautogroup_1435", "dealer_accounting_keyesmotors_1114", "dealer_accounting_ewingautogroup_1102", "dealer_accounting_ewingautogroup_1103", "dealer_accounting_houseofcars_1199", "dealer_accounting_bayouautogroup_1482", "dealer_accounting_houseofcars_1208", "dealer_accounting_dselite_tauranfoley_114", "dealer_accounting_tauranfoley_114", "dealer_accounting_anthonyautogroup_1476", "dealer_accounting_kengarffautomotive_1473", "dealer_accounting_beckmotors_1483", "dealer_accounting_mossmotors_1109"];
 
# checked = ["dealer_houseofcars_1208", "tenant_houseofcars", "dealer_dselite_tauranfoley_114", "tenant_dselite", "dealer_ewingautogroup_1103", "tenant_ewingautogroup", "dealer_tekiondeal_114", "tenant_tekiondeal", "dealer_bayouautogroup_1482", "tenant_bayouautogroup", "dealer_communityautomotive_1471", "tenant_communityautomotive", "dealer_bayouautogroup_1481", "dealer_mossmotors_1109", "tenant_mossmotors", "dealer_keyesmotors_1114", "tenant_keyesmotors", "dealer_kengarffautomotive_1473", "tenant_kengarffautomotive", "dealer_beckmotors_1483", "tenant_beckmotors", "dealer_ewingautogroup_1102", "dealer_houseofcars_1199", "dealer_tauranfoley_114", "tenant_tauranfoley", "dealer_ewingautogroup_1435", "dealer_anthonyautogroup_1476", "tenant_anthonyautogroup", "dealer_smpgroup_1193", "tenant_smpgroup", "dealer_crm_tauranfoley_114", "crm_tenant_tauranfoley", "dealer_crm_houseofcars_1208", "crm_tenant_houseofcars", "dealer_crm_ewingautogroup_1103", "crm_tenant_ewingautogroup", "dealer_crm_smpgroup_1193", "crm_tenant_smpgroup", "dealer_crm_ewingautogroup_1102", "dealer_crm_ewingautogroup_1435", "dealer_accounting_ewingautogroup_1102", "dealer_accounting_ewingautogroup_1103", "dealer_accounting_tekiondeal_114", "dealer_accounting_mossmotors_1109", "dealer_accounting_kengarffautomotive_1473", "dealer_accounting_anthonyautogroup_1476", "dealer_accounting_bayouautogroup_1482", "dealer_accounting_houseofcars_1199", "dealer_accounting_communityautomotive_1471", "dealer_accounting_houseofcars_1208", "dealer_accounting_beckmotors_1483", "dealer_accounting_bayouautogroup_1481", "dealer_accounting_smpgroup_1193", "dealer_accounting_keyesmotors_1114", "dealer_accounting_ewingautogroup_1435"]

taken = ['1', '2', '3', '4']
checked = ['1', '4', '5', '6', '7']
print(len(taken))
print(len(checked))




temp3 = [item for item in checked if item not in taken]
print(len(temp3))
print(temp3)

