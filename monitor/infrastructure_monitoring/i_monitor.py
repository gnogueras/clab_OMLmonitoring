'''
Created on Oct 23, 2014

@author: gerard
'''
import sys
import debug
from configuration import oldconfig
from couchbase_monitor.retriever import CouchBaseRetriever
from OML_Wrapper.wrapper import OMLWrapper
from utilities.utils import current_timestamp

def run():
    # retrieve monitoring info from CouchBase
    retriever = CouchBaseRetriever()
    metric = sys.argv[1]
    monitoringData = retriever.get_nodes_monitoring_metric(metric)
    # OML wrapper to convert the data into oml streams
    wrapper = OMLWrapper()
    wrapper.addMP(metric)
    wrapper.startOML()
    for v in monitoringData.itervalues():
        wrapper.injectData(metric, **v)
        #debug.printData(metric, **v)
    wrapper.closeOML()
    print "%s - Metric [%s] retrieved and injected into %s"%(current_timestamp(),metric,oldconfig.LOCAL_OML_SERVER)

if __name__ == '__main__':
    run()

# IMPORTANT! Call the script specifying the metric (availability, cpu, memory, runningvms, storage) as argument
# Ex: python i_monitor.py cpu

# Run command to add project to pythonpath
# export PYTHONPATH=$PYTHONPATH:/home/gerard/git/clab_OMLmonitoring/monitor/

# Run scripts with root permissions (imply sending icmp messages)
    
    

    
    
    
    