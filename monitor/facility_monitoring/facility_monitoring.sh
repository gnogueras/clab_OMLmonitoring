#!/bin/bash

##################################################################################################
#                                                                                                # 
# FACILITY MONITORING FOR C-LAB                                                                  #
# Run the script every 10 minutes (using crontab) to inject the facility monitoring data         #
# into the configured OML server(s)                                                              #
#                                                                                                #
# Use the command:                                                                               #
#	crontab -e                                                                               #
# to add the entry:                                                                              #
#       */10 * * * *  path_to_script/facility_monitoring.sh                                      #
#                                                                                                #
##################################################################################################

# Add project directory to python path
export PYTHONPATH=$PYTHONPATH:/home/gerard/git/clab_OMLmonitoring/monitor/

# Run script for Infrastructure monitoring
python /home/gerard/git/clab_OMLmonitoring/monitor/facility_monitoring/fac_monitor.py >> /home/gerard/facility_monitoring_log 2>&1

