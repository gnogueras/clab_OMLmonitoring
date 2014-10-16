'''
Created on Oct 16, 2014

@author: gerard
'''

import datetime
from oml4py import OMLBase

class OMLWrapper:

    def __init__ (self, appname=None, domain="CLab", sender="CLabTestbed", endpoint_uri=None):
        self.oml=OMLBase(appname, domain, sender, endpoint_uri)
    
    def addMP(self, metric, up=False, value=False):
        if up:
            schema = "node:string up:double last_check:string"
        if value:
            schema = "node:string value:string last_check:string"
        self.oml.addmp(metric, schema)
        
    def injectData(self, metric, node, data, timestamp=None):
        self.oml.start()
        self.oml.inject(metric, (node, data, self.get_timestamp(timestamp)))
        self.oml.close()
    
    def get_timestamp (self, timestamp=None):
        if not timestamp:
            ts=datetime.datetime.utcnow()
            return ts.strftime("%Y-%m-%d %H:%M:%S+00")
        else:
            # Format the timestamp from the CouchBase Monitor to match the format %Y-%m-%d %H:%M:%S+00
            return None
