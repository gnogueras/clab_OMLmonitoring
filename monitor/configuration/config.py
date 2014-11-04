'''
Created on Oct 20, 2014

@author: gerard

CONFIGURATION FILE FOR THE C-LAB MONITOR OF FED4FIRE
----------------------------------------------------------------------

This file includes all the parameters used in the scripts of the package. 
The values can be modified in this file, so no modifications are needed for the other files.

'''

### OML MONITORING ###
DOMAIN = 'CLab'
SENDER = 'CLab'
FACILITY_APP = 'FM'
INFRASTRUCTURE_APP = 'IM'
FM_APP = 'monitoringApp'
IM_APP = 'clab'
FM_NAME='CLabTestbed'

### OML SERVERS ###
FLS_OML_SERVER='tcp:flsmonitor.ilabt.iminds.be:3003'    # Fed4FIRE
TUB_OML_SERVER='tcp:193.175.132.241:3003'               # Technical University Berlin
LOCAL_OML_SERVER='tcp:localhost:3003'                   # Local server

### COMMUNITY-LAB CONTROLLER ###
CLAB_CONTROLLER_API='https://controller.community-lab.net/api/'
CLAB_CONTROLLER_URL='https://controller.community-lab.net/admin/'
CLAB_CONTROLLER_IPv4='84.88.85.17'
CLAB_CONTROLLER_IPv6='fdf5:5351:1d1f::2'

### COMMUNITY-LAB MONITORING SERVER ###
CLAB_MONITOR_IPV4='84.88.85.24'

### COMMUNITY-LAB COUCHBASE SERVER ###
COUCHBASE_HOST='http://monitor.confine-project.eu'
COUCHBASE_PORT=8091
COUCHBASE_BUCKET='newcurrent'
DESIGN_VIEW='dev_f4f_inf_mon'
VIEWS = dict( docs='get_nodes_docs', availability='get_nodes_availability', 
              cpu='get_nodes_cpu', memory='get_nodes_memory', info='get_nodes_info',
              storage='get_nodes_storage', runningvms='get_nodes_runningvms' )

### OML WRAPPER ###
MP = dict( 
           availability='availability', 
           cpu='cpu',
           memory='memory',            
           storage='storage', 
           runningvms='runningvms' 
        )
SCHEMA = dict( 
               availability='node:string up:int32 last_check:string', 
               cpu='node:string total:double free:double available:double last_check:string',
               memory='node:string total:double free:double available:double last_check:string', 
               storage='site:string storage:double last_check:string', 
               runningvms='node:string rvm:int32 last_check:string' 
              )

# LOCALHOST PSQL DB - OML BACKEND
DB_NAME = 'CLab'
DB_USER = 'oml'
DB_PASSWORD = 'fed4fire'
DB_HOST = 'localhost'
DB_TABLES=['clab_availability2','clab_cpu2','clab_memory2','clab_runningvms2','clab_storage2']

### DEFAULT OML SERVERS TO EXPORT MONITROING DATA ###
# Add other servers in the list if necessary
FACILITY_MON_SERVERS = [FLS_OML_SERVER, LOCAL_OML_SERVER]
INFRASTRUCTURE_MON_SERVERS = [LOCAL_OML_SERVER]
INFRASTRUCTURE_MON_METRICS = ['availability','cpu','memory','runningvms','storage']

