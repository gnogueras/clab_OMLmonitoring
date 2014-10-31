'''
Created on Oct 23, 2014

@author: gerard

INFRASTRUCTURE MONIORING FOR C-LAB
-----------------------------------
Simple version of the Facility Monitoring component.
The data is sent to the Fed4FIRE OML server (iMinds) and to the local OML server.

See/use fac_monitor.py
 
'''

from oml4py import OMLBase
import configuration.config as config
from utilities.ping_util import ping_ipv4_is_ok
from utilities.httpserver_util import website_is_ok
from utilities.utils import current_timestamp

def run ():

    oml=OMLBase(config.FM_APP, config.DOMAIN, config.SENDER, config.FLS_OML_SERVER)
    oml2=OMLBase(config.FM_APP, config.DOMAIN, config.SENDER, config.LOCAL_OML_SERVER)
    # MP for Controller Ping
    oml.addmp("icmp","node:string up:double last_check:string")
    oml2.addmp("icmp","node:string up:double last_check:string")
    # MP for Controller Http server (website)
    oml.addmp("http","node:string up:double last_check:string")
    oml2.addmp("http","node:string up:double last_check:string")
    
    controller_ping_up = ping_ipv4_is_ok(config.CLAB_CONTROLLER_IPv4)
    controller_http_up = website_is_ok(config.CLAB_CONTROLLER_URL)
    monitor_ping_up = ping_ipv4_is_ok(config.CLAB_MONITOR_IPV4)
    timestamp = current_timestamp()
    
    oml.start()
    oml.inject("icmp", ("controller", controller_ping_up, timestamp))
    oml.inject("http", ("controller", controller_http_up, timestamp))
    oml.close()
    
    oml2.start()
    oml2.inject("icmp", ("controller", controller_ping_up, timestamp))
    oml2.inject("http", ("controller", controller_http_up, timestamp))
    oml2.close()
    
    print "DONE " + current_timestamp()

if __name__ == '__main__':
    run()
    