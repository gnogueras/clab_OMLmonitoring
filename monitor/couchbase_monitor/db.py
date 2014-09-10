import os
from couchbase import Couchbase
from clab_monitoing import config
from clab_monitoing import util


class Database(object):

    def __init__(self, name):
        cb = Couchbase.connect(bucket=name, host='http://monitor.confine-project.eu', port=8091)
        # cb = Couchbase(config.DB_IP+":"+config.DB_PORT, "Administrator", "couchbase")
    
        #try:
        #    bucket = cb[name]
        #except:
        #   print ("No such bucket found in the Database!")
        #   exit(1)

        self.bucket = cb #bucket


    def get_bucket(self):
        return self.bucket


    def get_node_data_time_range(self, nodes, start_time="", end_time ="{}"):

        if not "" is start_time:
            start_time=util.convert_time_to_epoch(start_time)
            print "Start Time in epoch is: " + str(start_time)
        if not "{}" is end_time:
            end_time = util.convert_time_to_epoch(end_time)
            print "End Time in epoch is: " + str(end_time)

        os.makedirs("Nodes")
        for node_id in nodes:

            os.makedirs("Nodes/"+node_id)

            if(start_time==""):
                str_startkey = "[\"" + node_id + "\"]"
            else:
                str_startkey = "[\"" + node_id + "\"," + start_time+"]"

            str_endkey = "[\"" + node_id + "\"," + end_time+"]"

            #view_by_node_id = self.bucket.view('_design/node-timestamp/_view/get_node-timestamp', startkey=str_startkey, endkey = str_endkey, include_docs= True)
            view_by_node_id = self.bucket._view('_design/node-timestamp/_view/get_node-timestamp', startkey=str_startkey, endkey = str_endkey, include_docs= True)

            all_values = []

            for node in view_by_node_id:
                json = node['doc']
                document = json['json']
                meta = json['meta']
                id = meta['id']

                print id
                id = util.node_id_epoch_to_time(id)
                f = file("Nodes/"+node_id+"/"+id, 'w')
                f.write(str(document))
                f.close()
