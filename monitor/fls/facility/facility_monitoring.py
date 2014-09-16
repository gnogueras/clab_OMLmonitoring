'''
Created on Sep 5, 2014

@author: gerard
'''
import datetime
from oml4py import OMLBase
import fls.config
from ping.ping_util import ping_ipv4_is_ok
from httpserver.httpserver_util import website_is_ok

def run ():
    """
    Run the Facility Monitoring. Perform measurments and send it to FLS Server as OML Stream.
    Uses fls.config parameters.
    """
    oml=OMLBase("monitoringApp","CLab","CLabTestbed","tcp:flsmonitor.ilabt.iminds.be:3003")
    
    # MP for Controller Ping
    oml.addmp("icmp","node:string up:double last_check:string")
    
    # MP for Controller Http server (website)
    oml.addmp("http","node:string up:double last_check:string")
    
    controller_ping_up = ping_ipv4_is_ok(fls.config.CLAB_CONTROLLER_IPv4)
    controller_http_up = website_is_ok(fls.config.CLAB_CONTROLLER_URL)
    monitor_ping_up = ping_ipv4_is_ok(fls.config.CLAB_MONITOR_IPV4)
    
    oml.start()
    oml.inject("icmp", ("controller", controller_ping_up, current_timestamp()))
    oml.inject("http", ("controller", controller_http_up, current_timestamp()))
    oml.close()
    print "DONE " + current_timestamp()

def current_timestamp ():
    now=datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S+00")

if __name__ == '__main__':
    run()