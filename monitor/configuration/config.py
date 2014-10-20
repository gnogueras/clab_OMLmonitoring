'''
Created on Oct 20, 2014

@author: gerard
'''

FLS_OML_SERVER='tcp:flsmonitor.ilabt.iminds.be:3003'
FLS_OML_DOMAIN='CLab'
FLS_OML_NAME='CLabTestbed'

CLAB_CONTROLLER_URL='https://controller.community-lab.net/admin/'
CLAB_CONTROLLER_IPv4='84.88.85.17'
CLAB_CONTROLLER_IPv6='fdf5:5351:1d1f::2'

CLAB_MONITOR_IPV4='84.88.85.24'


COUCHBASE_HOST='http://monitor.confine-project.eu'
COUCHBASE_PORT=8091
COUCHBASE_BUCKET='test2'
VIEWS = dict(
                availability={'design':'all_nodes_availability', 'view':'get_all_nodes_availability'},
                cpu={'design':'all_nodes_cpu_total_perecent_usage', 'view':'get_all_nodes_cpu_total_perecent_usage'},
                disk={'design':'all_nodes_disk_total_percent_used', 'view':'get_all_nodes_disk_total_percent_used'},
                memory={'design':'all_nodes_memory_percent_used', 'view':'get_all_nodes_memory_percent_used'}
            )