'''
Created on Oct 23, 2014

@author: gerard

INFRASTRUCTURE MONIORING FOR C-LAB
-----------------------------------
Component that performs the infrastructure monitoring for the Community-Lab testbed 
in the context of the Fed4FIRE project.
The Monitor retrieves monitoring data about the nodes that integrate the testbed
from the CocuhBase database server used by Community-Lab,  
converts the data into OML streams,
and injects this data into the OML servers specified in the configuration file.

The monitored data consists of availability, cpu, memory, runningvms and storage metrics of the nodes.
By default, the OML servers the data is sent to is/are: local OML server

Optionally, you can add extra OML server endpoints to send the data to.
In the future, the users of the monitoring service might specify their own OML server to send the data to.
To deal with this requirement, you can add extra OML servers from the command line.
Ex: python infr_monitor.py tcp:extraOMLserver:3003

To run the Infrastructure monitoring, this Python script needs to be executed periodically.
To do that, use the shell script "infrastructure_monitoring.sh" included in the package.
The "infrastructure_monitoring.sh" generates a log file called "infrastructure_monitoring_log" in the /home directory.
Using crontab execute the "infrastructure_monitoring.sh" script every 5 minutes.

NOTE: to execute the python script, the /monitor directory containing this package needs to be included
to the python path. (export PYTHONPATH=$PYTHONPATH:path_to_monitor_dir/monitor/)

'''

import sys
import debug
from configuration import config
from couchbase_monitor.retriever import CouchBaseRetriever
from OML_Wrapper.wrapper import OMLWrapper
from utilities.utils import current_timestamp

def run(*argv):
    
    oml_servers = config.INFRASTRUCTURE_MON_SERVERS;
    if argv: oml_servers.extend(argv)
    
    for metric in config.INFRASTRUCTURE_MON_METRICS:
        # retrieve monitoring info from CouchBase
        retriever = CouchBaseRetriever()
        monitoringData = retriever.get_nodes_monitoring_metric(metric)
         
        for server in oml_servers:   
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
    argv = sys.argv
    del argv[0]
    run(*argv)


    

    
    
    
    