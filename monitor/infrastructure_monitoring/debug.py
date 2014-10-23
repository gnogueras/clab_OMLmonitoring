'''
Created on Oct 23, 2014

@author: gerard
'''

from utilities.utils import epoch_to_utc


# Functions that print the results of the retrieve operation for DEBUG purposes

def printData(metric, **kwargs):
    if metric == 'availability': 
        print kwargs['node'] + "  up=" + str(kwargs['up']) + "  last_check: " + epoch_to_utc(kwargs['timestamp'])
    elif metric == 'cpu': 
        print kwargs['node']+ "  total=" + str(kwargs['total'])+ "  free=" + str(kwargs['free'])+ "  available=" + str( kwargs['available']) + "  last_check: " + epoch_to_utc(kwargs['timestamp'])
    elif metric == 'memory': 
        print kwargs['node']+ "  total=" + str(kwargs['total'])+ "  free=" + str(kwargs['free'])+ "  available=" + str( kwargs['available']) + "  last_check: " + epoch_to_utc(kwargs['timestamp'])
    elif metric == 'runningvms': 
        print kwargs['node']+ "  rvm=" + str(kwargs['rvm']) + "  last_check: " + epoch_to_utc(kwargs['timestamp'])
    elif metric == 'storage': 
        print kwargs['site']+ "  storage=" + str(kwargs['storage']) + "  last_check: " + epoch_to_utc(kwargs['timestamp'])       