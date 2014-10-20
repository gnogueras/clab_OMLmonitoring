'''
Created on Oct 16, 2014

@author: gerard
'''

from utilities.utils import get_timestamp 
from oml4py import OMLBase

class OMLWrapper:

    def __init__ (self, appname=None, domain="CLab", sender="CLabTestbed", endpoint_uri=None):
        self.oml=OMLBase(appname, domain, sender, endpoint_uri)
    
    def addMP(self, metric, up=None, used=None, total=None):
        if up:
            schema = "node:string up:double last_check:string"
        elif used and total:
            schema = "node:string total:string used:string last_check:string"
        self.oml.addmp(metric, schema)
        
    def injectData(self, metric, node, up=None, used=None, total=None, timestamp=None):
        self.oml.start()
        if up:
            self.oml.inject(metric, (node, up, get_timestamp(timestamp)))
        elif used and total:
            self.oml.inject(metric, (node, used, total, get_timestamp(timestamp)))
        self.oml.close()
    

