'''
Created on Oct 23, 2014

@author: gerard
'''

import debug
from configuration import config
from couchbase_monitor.retriever import CouchBaseRetriever
from OML_Wrapper.wrapper import OMLWrapper
from utilities.utils import current_timestamp

def run():
    for metric in config.INFRASTRUCTURE_MON_METRICS:
        # retrieve monitoring info from CouchBase
        retriever = CouchBaseRetriever()
        monitoringData = retriever.get_nodes_monitoring_metric(metric)
         
        for server in config.INFRASTRUCTURE_MON_SERVERS:   
            # OML wrapper to convert the data into oml streams
            wrapper = OMLWrapper(endpoint_uri=server)
            wrapper.addMP(metric)
            wrapper.startOML()
            for v in monitoringData.itervalues():
                wrapper.injectData(metric, **v)
                #debug.printData(metric, **v)
            wrapper.closeOML()
            print "%s - Infrastructure Monitoring:  [%s] retrieved and injected into %s"%(current_timestamp(),metric,server)

if __name__ == '__main__':
    run()

# IMPORTANT! Call the script specifying the metric (availability, cpu, memory, runningvms, storage) as argument
# Ex: python i_monitor.py cpu

# Run command to add project to pythonpath
# export PYTHONPATH=$PYTHONPATH:/home/gerard/git/clab_OMLmonitoring/monitor/

# Run scripts with root permissions (imply sending icmp messages)
    
    

    
    
    
    