'''
Created on Oct 21, 2014

@author: gerard
'''
from couchbase import Couchbase
from couchbase.views.iterator import View
from couchbase.views.params import Query
from utilities.ping_util import ping_ipv6_is_ok
from utilities.utils import get_timestamp
from orm.api import Api
from utilities.utils import epoch_to_utc, bits_to_bytes, node_ipv6_to_name, current_timestamp, get_node_current_state
import time
import configuration.config as config

class CouchBaseRetriever:
    
    def __init__(self):
        # connection to CouchBase DB
        self.cb = Couchbase.connect(bucket=config.COUCHBASE_BUCKET, host=config.COUCHBASE_HOST, port=config.COUCHBASE_PORT)
        # connection to Testbed Controller
        self.controller = Api(config.CLAB_CONTROLLER_API)
        
        
    def get_monitoring_metrics_all_nodes(self, metric):
        view=View(self.cb, self.VIEW['design'], self.VIEW['view'], include_docs=True, full_set=True)
        nodes_info={}
        for v in view:
            nodes_info[v.key]=v.value                
        if metric=='availability':
            return self.get_availability_all_nodes(nodes_info)
        elif metric=='cpu':
            return self.get_availability_all_nodes(nodes_info)
        elif metric=='disk':
            return self.get_availability_all_nodes(nodes_info)
        elif metric=='memory':
            return self.get_availability_all_nodes(nodes_info)

    
    def get_availability_all_nodes(self, nodes_info):
        nodes = self.controller.nodes.retrieve()
        results = {}
        for node in nodes:
            addr = node.mgmt_net.addr
            up = addr in nodes_info
            ts = current_timestamp()
            results[addr]={'value':up, 'timestamp': ts}
        # results = { node_ipv6 : { value : val , timestamp : ts} }
        return results
    
    def get_cpu_all_nodes(self, nodes_info):
        results = {}
        for node in nodes_info.values():
            results[node['nodeid']] = { 'total': node['cpu']['num_cpus'],
                                        'used': node['cpu']['total_percent_usage'],
                                        'timestamp' : epoch_to_utc(node['timestamp'])}       
        # results = { node_ipv6 : { value : val , timestamp : ts} }
        return results
  
    def get_disk_all_nodes(self, nodes_info):
        total=float(0) 
        used=float(0)
        results = {}
        for node in nodes_info.values():
            for k,v in node['disk'].items():
                if k!='size':
                    total=total+v['total']
                    used=used+v['used']       
            results[node['nodeid']] = { 'total': bits_to_bytes(node['disk']['size']),
                                        'used': round(used*100/total,2),
                                        'timestamp' : epoch_to_utc(node['timestamp'])}       
        # results = { node_ipv6 : { value : val , timestamp : ts} }
        return results
  
  
    def get_memory_all_nodes(self, nodes_info):
        results = {}
        for node in nodes_info.values():
            results[node['nodeid']] = { 'total': bits_to_bytes(node['memory']['total']),
                                        'used': node['memory']['percent_used'],
                                        'timestamp' : epoch_to_utc(node['timestamp'])}       
        # results = { node_ipv6 : { value : val , timestamp : ts} }
        return results
  
  
  
        
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
        
        results = {}
        view=View(self.cb,"dev_nodeinfo","nodeinfo", include_docs=True)
        for v in view:
            results[v.key] = v.value
    
    def get_monitoring_metrics_all_nodes2(self, metric):
        if metric=='availability':
            return self.get_availability_all_nodes()
        # metric = availability, cpu, disk, memory
        doc = self.VIEWS[metric]
        view=View(self.cb,doc['design'],doc['view'], include_docs=True)
        
        results = {}
        for v in view:
            results[v.key] = v.value
        # results = { node_ipv6 : { value : val , timestamp : ts} }
        return results
        
    def get_availability_all_nodes2(self):
        nodes = self.controller.nodes.retrieve()
        results = {}
        for node in nodes:
            addr = node.mgmt_net.addr
            up = ping_ipv6_is_ok(addr)
            results[addr]={'value':up, 'timestamp': get_timestamp()}
        # results = { node_ipv6 : { value : val , timestamp : ts} }
        return results
    
    def get_nodes_monitoring_metric3(self, metric):
        if metric == 'availability':
            return self.get_nodes_availability2()
        print "not availability"
        view=View(self.cb, config.DESIGN_VIEW, config.VIEWS[metric], include_docs=True, full_set=True)
        nodes_info={}
        for v in view:
            node_name=node_ipv6_to_name(self.api, v.value['nodeid'])
            nodes_info[node_name]=v.value
        return nodes_info
    
    def get_nodes_availability3(self):
        nodes = self.api.nodes.retrieve()
        nodes_availability = {}
        timestamp = current_timestamp()
        for node in nodes:
            current_state = get_node_current_state(self.api, node)
            up = 1 if current_state=='production' else 0
            addr = "[{0}]".format(node.mgmt_net.addr)
            nodes_availability[node.name]={'nodeid':addr, 'timestamp': timestamp, 'up':up}
        return nodes_availability
