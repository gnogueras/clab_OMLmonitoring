'''
Created on Oct 23, 2014

@author: gerard

FACILITY MONIORING FOR C-LAB
-----------------------------------

Component that performs the facility monitoring for the Community-Lab testbed 
in the context of the Fed4FIRE project.
The Monitor itself gets the facility monitoring data that consists of double variables used as boolean 
to indicate if the ping to the controller and the webserver in the controller machine are working correctly. 
This data is converted into OML streams,
and injected into the OML servers specified in the configuration file.

By default, the OML servers the data is sent to is/are: local OML server, Fed4FIRE OML server (iMinds, FirstLevelSupport)

To run the Facility monitoring, this Python script needs to be executed periodically with ROOT permissions,
since the icmp operations required ROOT permissions.
To do that, use the shell script "facility_monitoring.sh" included in the package.
The "facility_monitoring.sh" generates a log file called "facility_monitoring_log" in the /home directory.
Using crontab (of ROOT user) execute the "facility_monitoring.sh" script every 10 minutes.

NOTE: to execute the python script, the /monitor directory containing this package needs to be included
to the python path. (export PYTHONPATH=$PYTHONPATH:path_to_monitor_dir/monitor/)

IMPORTANT: the facility_monitoring.py script needs to be executed with ROOT permissions.
Add crontab entry in the crontab file of the ROOT user.

'''

from oml4py import OMLBase
from utilities.ping_util import ping_ipv4_is_ok
from utilities.httpserver_util import website_is_ok
from utilities.utils import current_timestamp
from configuration import config

def run ():
    for server in config.FACILITY_MON_SERVERS:

        oml=OMLBase(config.FM_APP, config.DOMAIN, config.SENDER, server)
        # MP for Controller Ping
        oml.addmp("icmp","node:string up:double last_check:string")
        # MP for Controller Http server (website)
        oml.addmp("http","node:string up:double last_check:string")
        
        controller_ping_up = ping_ipv4_is_ok(config.CLAB_CONTROLLER_IPv4)
        controller_http_up = website_is_ok(config.CLAB_CONTROLLER_URL)
        monitor_ping_up = ping_ipv4_is_ok(config.CLAB_MONITOR_IPV4)
        timestamp = current_timestamp()
        
        oml.start()
        oml.inject("icmp", ("controller", controller_ping_up, timestamp))
        oml.inject("http", ("controller", controller_http_up, timestamp))
        oml.close()

        print current_timestamp()+" - Facilitity Monitoring: data sent to "+server

if __name__ == '__main__':
    run()