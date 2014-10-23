'''
Created on Oct 16, 2014

@author: gerard
'''

from utilities.utils import epoch_to_utc
from configuration import config 
from oml4py import OMLBase

class OMLWrapper:

    def __init__ (self, appname=config.IM_APPNAME, domain=config.IM_DOMAIN, sender=config.IM_SENDER, endpoint_uri=config.TUB_OML_SERVER):
        self.oml=OMLBase(appname, domain, sender, endpoint_uri)
    
    def addMP(self, metric, schema=None):
        if not schema:
            schema = config.SCHEMA[metric]
        self.oml.addmp(metric, schema)

        
    def injectData(self, metric, **kwargs):
        if metric == 'availability': 
            self.oml.inject(metric, (kwargs['node'], kwargs['up'], epoch_to_utc(kwargs['timestamp'])))
        elif metric == 'cpu': 
            self.oml.inject('cpu', (kwargs['node'], kwargs['total'], kwargs['free'], kwargs['available'], epoch_to_utc(kwargs['timestamp'])))
        elif metric == 'memory': 
            self.oml.inject(metric, (kwargs['node'], kwargs['total'], kwargs['free'], kwargs['available'], epoch_to_utc(kwargs['timestamp'])))
        elif metric == 'runningvms': 
            self.oml.inject(metric, (kwargs['node'], kwargs['rvm'], epoch_to_utc(kwargs['timestamp'])))
        elif metric == 'storage': 
            self.oml.inject(metric, (kwargs['site'], kwargs['storage'], epoch_to_utc(kwargs['timestamp'])))         
    
    def startOML(self):
        self.oml.start()

    def closeOML(self):
        self.oml.close()

    

