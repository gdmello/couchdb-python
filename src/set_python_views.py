import ConfigParser

couchdb_local_ini = '/usr/local/etc/couchdb/local.ini'

config = ConfigParser.ConfigParser()
config.read(couchdb_local_ini)
config.set('query_servers', 'python', 'couchpy')

with open(couchdb_local_ini, 'wb') as config_file:
    config.write(config_file)

