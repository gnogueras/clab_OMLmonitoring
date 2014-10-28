'''
Created on Sep 5, 2014

@author: gerard
'''
from oml4py import OMLBase
from utilities.ping_util import ping_ipv4_is_ok
from utilities.httpserver_util import website_is_ok
from utilities.utils import current_timestamp
from configuration import config

def run ():
    """
    Run the Facility Monitoring. Perform measurements and send it to FLS Server as OML Stream.
    Uses facility_monitoring.oldconfig parameters.
    """
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