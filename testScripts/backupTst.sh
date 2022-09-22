#!/bin/bash
startdate=$(date -u +"%s")
while getopts d: flag
do
    case "${flag}" in
        d) databaseName=${OPTARG};;
        *) echo "ERROR : please check arguments"
    esac
done
echo ${databaseName}

if [[ $(echo "db.getMongo().getDBNames()" | mongo --host "rsnew1/172.31.255.99:27017,172.31.203.137:27017,172.31.169.125:27017,172.31.184.237:27017" --authenticationDatabase "admin" --username rootdba -p sCNVdKXyOba1Se) =~ "\"${databaseName}\""  ]]  && [[ $(echo "db.getMongo().getDBNames()" | mongo --host "rsnew2/172.31.141.190:27017,172.31.189.100:27017,172.31.134.113:27017" --authenticationDatabase "admin" --username "rootdba" --password "sCNVdKXyOba1Se") =~ "\"${databaseName}\""  ]];
then 

      echo "the ${databaseName} is  present in both clusters"

elif [[ $(echo "db.getMongo().getDBNames()" | mongo --host "rsnew1/172.31.255.99:27017,172.31.203.137:27017,172.31.169.125:27017,172.31.184.237:27017" --authenticationDatabase "admin" --username rootdba -p sCNVdKXyOba1Se) =~ "${databaseName}" ]]; 
then

      sudo mongodump --host "rsnew1/172.31.137.253:27017,172.31.255.99:27017,172.31.203.137:27017,172.31.169.125:27017,172.31.184.237:27017" --authenticationDatabase "admin" --username rootdba --password sCNVdKXyOba1Se --db ${databaseName} --forceTableScan --gzip --out /home/ubuntu/golive/`date +"%Y%m%d"`/Preprod_backup/ 

elif [[ $(echo "db.getMongo().getDBNames()" | mongo --host "rsnew2/172.31.141.190:27017,172.31.189.100:27017,172.31.134.113:27017" --authenticationDatabase "admin" --username "rootdba" --password "sCNVdKXyOba1Se") =~ "${databaseName}" ]]; 
then

      sudo mongodump --host "rsnew2/172.31.141.190:27017,172.31.189.100:27017,172.31.134.113:27017" --authenticationDatabase "admin" --username rootdba --password sCNVdKXyOba1Se --db ${databaseName} --forceTableScan --gzip --out /home/ubuntu/golive/`date +"%Y%m%d"`/Preprod_backup/ 

else echo "The database is not present in Both PREPROD clusters"
fi

enddate=$(date -u +"%s")
echo "Time taken for dump : $(date -u -d "0 $enddate sec - $startdate sec" +"%H:%M:%S")"


if [[ $(echo "db.getMongo().getDBNames()" | mongo --host "atlas-107srg-shard-0/crm-shard-00-02.jamvq.mongodb.net:27017,crm-shard-00-01.jamvq.mongodb.net:27017,crm-shard-00-00.jamvq.mongodb.net:27017,crm-shard-00-03.jamvq.mongodb.net:27017" --ssl --username kavithap_prod --password dba@123A  --authenticationDatabase admin) =~ "${databaseName}" ]]; 
then

  echo "EXIT: the ${databaseName} is in CRM prod "
  exit

else echo "The database is not present in CRM PROD cluster"
fi



startdate=$(date -u +"%s")

#sudo aws s3 cp --recursive /home/ubuntu/golive/`date +"%Y%m%d"`/ s3://dms-prod-mongo-backup/golive_jenkins_backups/`date +"%Y%m%d"`/ 

#sudo mongorestore --host "atlas-107srg-shard-0/crm-shard-00-02.jamvq.mongodb.net:27017,crm-shard-00-01.jamvq.mongodb.net:27017,crm-shard-00-00.jamvq.mongodb.net:27017,crm-shard-00-03.jamvq.mongodb.net:27017" --ssl --username --authenticationDatabase admin --db ${databaseName} --drop --gzip /home/ubuntu/golive/`date +"%Y%m%d"`/Preprod_backup/${databaseName}/ 
echo "mongorestore on prod"
enddate=$(date -u +"%s")
echo "Time taken to restore: $(date -u -d "0 $enddate sec - $startdate sec" +"%H:%M:%S")"






