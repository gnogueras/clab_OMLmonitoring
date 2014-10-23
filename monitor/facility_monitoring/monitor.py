'''
Created on Sep 5, 2014

@author: gerard
'''
from oml4py import OMLBase
import configuration.config as config
from utilities.ping_util import ping_ipv4_is_ok
from utilities.httpserver_util import website_is_ok
from utilities.utils import current_timestamp

def run ():
    """
    Run the Facility Monitoring. Perform measurments and send it to FLS Server as OML Stream.
    Uses facility_monitoring.config parameters.
    """
    oml=OMLBase(config.FM_APP, config.FM_DOMAIN, config.FM_NAME, config.FLS_OML_SERVER)
    
    # MP for Controller Ping
    oml.addmp("icmp","node:string up:double last_check:string")
    
    # MP for Controller Http server (website)
    oml.addmp("http","node:string up:double last_check:string")
    
    controller_ping_up = ping_ipv4_is_ok(config.CLAB_CONTROLLER_IPv4)
    controller_http_up = website_is_ok(config.CLAB_CONTROLLER_URL)
    monitor_ping_up = ping_ipv4_is_ok(config.CLAB_MONITOR_IPV4)
    
    oml.start()
    oml.inject("icmp", ("controller", controller_ping_up, current_timestamp()))
    oml.inject("http", ("controller", controller_http_up, current_timestamp()))
    oml.close()
    print "DONE " + current_timestamp()

if __name__ == '__main__':
    run()