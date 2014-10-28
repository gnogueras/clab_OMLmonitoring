'''
Created on Sep 18, 2014

@author: gerard
'''
from couchbase import Couchbase
from couchbase.views.iterator import View
from orm.api import Api
from utilities.utils import current_epoch_timestamp, unicode_normalize
from configuration import config
import collections

class CouchBaseRetriever:
    
    def __init__(self):
        # connection to CouchBase DB
        self.cb = Couchbase.connect(bucket=config.COUCHBASE_BUCKET, host=config.COUCHBASE_HOST, port=config.COUCHBASE_PORT)
        # connection to C-Lab Controller API
        self.api = Api(config.CLAB_CONTROLLER_API)
        self.api.retrieve()
    
    def get_nodes_monitoring_metric(self, metric):
        view=View(self.cb, config.DESIGN_VIEW, config.VIEWS[metric], include_docs=True, full_set=True)
        nodes_info={}
        for v in view:
            node_name=v.value['node']
            nodes_info[node_name]=v.value
        if metric == 'availability':
            return self.get_nodes_availability(nodes_info)
        return collections.OrderedDict(sorted(nodes_info.items()))

    
    def get_nodes_availability(self, nodes_info):
        nodes = self.api.nodes.retrieve()
        nodes_availability = {}
        timestamp = current_epoch_timestamp()
        for node in nodes:
            addr = "[{0}]".format(node.mgmt_net.addr)
            current_state= nodes_info[node.name]['current_state'] if node.name in nodes_info else 'UNKNOWN'
            up = 1 if current_state=='production' else 0
            nodes_availability[node.name]={'node':unicode_normalize(node.name), 'node_addr':addr, 'timestamp':timestamp, 'up':up, 'current_state':current_state}
        return collections.OrderedDict(sorted(nodes_availability.items()))
    

    
    
    
        