'''
Created on Oct 20, 2014

@author: gerard
'''
# Run command to add project to pythonpath
# export PYTHONPATH=$PYTHONPATH:/home/gerard/git/clab_OMLmonitoring/monitor/

# PYTHONPATH=/home/gerard/git/clab_OMLmonitoring/monitor/ python /home/gerard/git/clab_OMLmonitoring/monitor/facility_monitoring/monitor.py >> /home/gerard/fls_log 2>&1

# Run scripts FLS with root permissions (imply sending icmp messages)

### COMMUNITY-LAB CONTROLLER ###
CLAB_CONTROLLER_API='https://controller.community-lab.net/api/'
CLAB_CONTROLLER_URL='https://controller.community-lab.net/admin/'
CLAB_CONTROLLER_IPv4='84.88.85.17'
CLAB_CONTROLLER_IPv6='fdf5:5351:1d1f::2'


### COMMUNITY-LAB MONITORING SERVER ###
CLAB_MONITOR_IPV4='84.88.85.24'


### FED4FIRE FLS OML SERVER ### 
FLS_OML_SERVER='tcp:flsmonitor.ilabt.iminds.be:3003'

### TUB OML SERVER ### 
TUB_OML_SERVER='tcp:193.175.132.241:3003'

### LOCAL OML SERVER ###
LOCAL_OML_SERVER='tcp:localhost:3003'

### FACILITY MONITORING ###
FM_APP='monitoringApp'
FM_DOMAIN='CLab'
FM_NAME='CLabTestbed'

### INFRASTRUCTURE MONITORING ###
IM_APPNAME='clab'
IM_DOMAIN='CLab'
IM_SENDER='CLab'


### COMMUNITY-LAB COUCHBASE SERVER ###
COUCHBASE_HOST='http://monitor.confine-project.eu'
COUCHBASE_PORT=8091
COUCHBASE_BUCKET='newcurrent'
DESIGN_VIEW='dev_f4f_inf_mon'
VIEWS = dict( docs='get_nodes_docs', availability='get_nodes_availability', 
              cpu='get_nodes_cpu', memory='get_nodes_memory', info='get_nodes_info',
              storage='get_nodes_storage', runningvms='get_nodes_runningvms' )


### OML WRAPPER
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


