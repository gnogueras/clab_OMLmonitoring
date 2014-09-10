import calendar
import time
import os

def convert_time_to_epoch(date_time,pattern = '%Y-%m-%d'):
    #date_time = '2007-02-05'

    epoch = str(calendar.timegm(time.strptime(date_time, pattern)))
    return epoch

def ensure_dir(d):
   if not os.path.exists(d):
        os.makedirs(d)


def convert_epoch_to_date_time(epoch):
    date_time= time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(float(epoch)))
    return str(date_time)

def node_id_epoch_to_time(name):
    (node_id, epoch) = name.split("-")
    time = convert_epoch_to_date_time(epoch)
    return str(node_id+'-'+time)