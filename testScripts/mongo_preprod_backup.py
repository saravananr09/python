

db_config_node0 = {'username': "srajendran_pre", 'password': "xresaas", 'nodes': ["node0", "node1", "node2"], 'replSetName': "rsnewx", 'clusterType': "onprem"}

def db_connection_arguments(db_creds: dict):
    # nodeList = [node for node in db_creds['nodes']]
    host = f"{db_creds['replSetName']}/{','.join(db_creds['nodes'])}"
    username = db_creds['username']
    password = db_creds['password']
    extraAruguments = "--authenticationDatabase adminos" if db_creds['clusterType'] == 'onprem' else "--ssl --authenticationDatabase admin"
    return f" --host '{host}' {extraAruguments} --username {username} --password {password} "

import os, uuid, subprocess
backup_dir_path = os.path.expanduser('~') + "/preprod_backups"
secret_key = str(uuid.uuid4().hex[:16])
database_creds = db_connection_arguments(db_config_node0)
