'''
Created on Sep 18, 2014

@author: gerard
'''
from couchbase import Couchbase
from couchbase.views.iterator import View
from couchbase.views.params import Query
from orm.api import Api

class CouchBaseRetriever:
    
    def __init__(self):
        # connection to CouchBase DB
        self.cb = Couchbase.connect(bucket='new', host='http://monitor.confine-project.eu', port=8091)
        # connection to Testbed Controller
        self.controller = Api('https://controller.community-lab.net/api/')
    
    
    def get_monitoring_metric_single_node(self, metric, node_uri):
        
        # GET VIEW
        view=View(self.cb,"node-mostrecent","get_node-mostrecent", include_docs=True)
        
        # GET VIEW WITH QUERY, FILTER
        q=Query()
        q.key='[fdf5:5351:1dfd:b1::2]'
        view=View(self.cb,"node-mostrecent","get_node-mostrecent", include_docs=True, query=q)
        
        # GET MONITORING PARAMETER
        for v in view: r=v
        r.doc.value['load_avg']
    
    def get_node_ipv6(self, node_uri):
        node=self.controller.retrieve(node_uri)
        return node.mgmt_net.addr
        
        