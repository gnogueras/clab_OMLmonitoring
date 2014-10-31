#!/bin/bash

##################################################################################################
#                                                                                                # 
# INFRASTRUCTURE MONITORING FOR C-LAB                                                            #
# Run the script every 5 minutes (using crontab) to inject the infrastructure monitoring data    #
# into the configured OML server(s)                                                              #
#                                                                                                #
# Use the command:                                                                               #
#	crontab -e                                                                               #
# to add the entry:                                                                              #
#       */10 * * * *  path_to_script/infrastructure_monitoring.sh                                #
#                                                                                                #
##################################################################################################

# Add project directory to python path
export PYTHONPATH=$PYTHONPATH:/home/gerard/git/clab_OMLmonitoring/monitor/

# Run script for Infrastructure monitoring
python /home/gerard/git/clab_OMLmonitoring/monitor/infrastructure_monitoring/infr_monitor.py >> /home/gerard/infrastructure_monitoring_log 2>&1

