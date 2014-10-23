'''
Created on Oct 16, 2014

@author: gerard
'''
import time, unicodedata
from ast import literal_eval

def current_epoch_timestamp ():
    return time.time()

def epoch_to_utc(epoch):
    return time.strftime('%Y-%m-%d %H:%M:%S+00', time.gmtime(epoch))


def current_timestamp ():
    return epoch_to_utc(time.time())
    #now=datetime.datetime.utcnow()
    #return now.strftime("%Y-%m-%d %H:%M:%S+00")
    
    
def get_node_ipv6(api, node_uri):
    node=api.retrieve(node_uri)
    return node.mgmt_net.addr


def node_ipv6_to_name(api, ipv6):
    node_url = "http://{0}/confine/api/node/".format(ipv6)
    try:
        node = api.retrieve(node_url)
        return node.name
    except:
        print "RETRIEVE FAILED: "+node_url
        return ipv6

def get_node_current_state(api, node):
        node.retrieve()
        state_link = node.get_links()['http://confine-project.eu/rel/controller/state']
        current_state = literal_eval(api.get(state_link).content.replace('null','"null"'))
        return current_state['current']


def bits_to_bytes(bits):
    bytes=float(bits)
    while bytes >= 1024:
        bytes=bytes/1024
    return round(bytes,2)

def unicode_normalize(name):
    return unicodedata.normalize('NFKD', name).encode('ascii','ignore')
