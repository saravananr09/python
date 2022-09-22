db.getCollectionNames().forEach(function (col) {
    var dataCount = db[col].count();
    var idxCount = db[col].getIndexes().length;
    print(col, dataCount, idxCount)
});


db.getMongo().getDBNames().forEach((dbs) => {
    ignore_dbs = ["local", "admin", "config"]
    db_type = dbs.split('_')[0];
    if (!ignore_dbs.includes(dbs)) {
        if (db_type == 'dealer') {
            db = db.getSiblingDB(dbs)
            var doc_count = db.ServiceVehicleARC.count()
            print(db, "-" ,doc_count)
            print("Doc Count - ", )
            var idx_details = db.ServiceVehicleARC.getIndexes()
            idx_details.forEach((idxs) => {
                print(idxs.name)
                    printjson(idxs.key)
                        print(idxs.unique)
            })      
        }
    }
})


db.getCollectionNames().forEach(function(col) {
    var indexes = db[col].getIndexes();
    indexes.forEach(function (c) {
        var fields = '', result = '', options = {};
        for (var i in c) {
            if (i == 'key') {
                fields = c[i];
            } else if (i == 'name' && c[i] == '_id_') {
                return;
            } else if ( i != 'v' && i != 'ns') {
                options[i] = c[i];
            }
        }
        options["background"] = true;

        var fields = JSON.stringify(fields);
        var options = JSON.stringify(options);
        if (options == '{}') {
            result = "db." + col + ".createIndex(" + fields + "); ";
        } else {
            result = "db." + col + ".createIndex(" + fields + ", " + options + "); ";
        }
        result = result
            .replace(/{"floatApprox":-1,"top":-1,"bottom":-1}/ig, '-1')
            .replace(/{"floatApprox":(-?\d+)}/ig, '$1')
            .replace(/\{"\$numberLong":"(-?\d+)"\}/ig, '$1');
        print(result);
    });
});