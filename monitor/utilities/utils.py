'''
Created on Oct 16, 2014

@author: gerard
'''
import datetime, time
from orm.api import Api


def get_timestamp (timestamp=None):
    if not timestamp:
        ts=datetime.datetime.utcnow()
        return ts.strftime("%Y-%m-%d %H:%M:%S+00")
    else:
        # Format the timestamp from the CouchBase Monitor to match the format %Y-%m-%d %H:%M:%S+00
        return None


def current_timestamp ():
    now=datetime.datetime.utcnow()
    return now.strftime("%Y-%m-%d %H:%M:%S+00")


def epoch_to_utc(self, epoch):
    time.strftime('%Y-%m-%d %H:%M:%S+00', time.localtime(epoch))
    
    
def get_node_ipv6(self, node_uri):
    node=self.controller.retrieve(node_uri)
    return node.mgmt_net.addr


def node_ipv6_to_name(self, api, ipv6):
    node_url = "http://{0}/confine/api/node/".format(ipv6)
    node = api.retrieve(node_url)
    return node.name

def bits_to_bytes(self, bits):
    bytes=float(bits)
    while bytes >= 1024:
        bytes=bytes/1024
    return round(bytes,2)