from couchbase_monitor import controller
from couchbase_monitor import nodelist
from couchbase_monitor import db

if __name__ == '__main__':
    controller.update_node_list()
    nodes = nodelist.get_node_list()
    bucket = db.Database("test")
    bucket.get_node_data_time_range(nodes, "2014-04-07", "2014-05-11")