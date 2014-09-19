from couchbase_monitor.nava import controller
from couchbase_monitor.nava import nodelist
from couchbase_monitor.nava import db

if __name__ == '__main__':
    controller.update_node_list()
    nodes = nodelist.get_node_list()
    bucket = db.Database("test")
    bucket.get_node_data_time_range(nodes, "2014-04-07", "2014-05-11")