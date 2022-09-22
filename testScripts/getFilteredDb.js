// db.getMongo().getDBNames().forEach(
//     (dbs) => {
//         var filterDealer = dbs.split('_')[0];
//         var filterCrm = dbs.split('_')[1]
//         if (filterDealer == 'dealer' && filterCrm != 'crm') {
//             var collCount = db.getSiblingDB(dbs).getCollection('pdfDocument').count()
//             if (collCount > 0) {
//                 print(dbs, collCount)
//             }
//         }
//     })

var getDB = ((databases_ar, dbType) => {
    database_type = dbType;
    filteredDBList = [];
    databases_ar.forEach((dbs) => {
        var firElement = dbs.split('_')[0];
        var secElement = dbs.split('_')[1];
        if (database_type == 'DMS') {
            if ((firElement == 'dealer' || firElement == 'tenant') && (secElement!='crm')) {
                print(dbs)
            }
        } 
        else if(database_type == 'CRM') {
            if((firElement == 'dealer' && secElement == 'crm') || (firElement == 'crm' && secElement == 'tenant')) {
                print(dbs)
            }
        }
    })
})
var databases_ar = db.getMongo().getDBNames();
getDB(databases_ar, 'DMS');     
getDB(databases_ar, 'CRM');     


databases_ar.forEach((dbs) => {
    //print(dbs, db.getSiblingDB(dbs).getCollection('coll_idx_test').count());
    db = db.getSiblingDB(dbs);
    if (db.stats().collections > 0) {
        dealerColls = ['templateStore', 'dynamicTag', ];
        tenantColls = ['userSignatureSetup', 'templateSetup'];
      
    }
})