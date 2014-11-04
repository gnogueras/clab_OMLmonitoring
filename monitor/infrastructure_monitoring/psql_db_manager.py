'''
Created on Nov 3, 2014

@author: gerard

SCRIPT TO MANAGE THE POSTGRESQL DATABASE USED AS BACKEND OF OML SEVER
---------------------------------------------------------------------

This Python script provides some function to manage the database. The information of
the database and tables, as well as the user and password to connect to it can be found in the configuration 
file (configuration/config.py).

By default the script works with the database "CLab" as "oml" user, and acts on the tables
"clab_availability, clab_cpu, clab_memory, clab_runningvms, clab_storage", 
which correspond to the infrastructure monitoring component.

The script has two different uses:

1. Delete duplicates: delete the duplicate entries (same node name and same last_check timestamp) found in the tables. 
To use the script to delete duplicates, execute the command:

     python psql_db_manager.py delete_duplicates

2. Clear the database: clearing the database includes the previous delete duplicates operation. Moreover, this operation takes an
integer parameter that defines the maximum number of entries to keep for each node. Thus, if there are 100 entries for the Node1, 
and the parameter of the function is 10, the clearing operation will only keep the 10 most recent entries for Node1 and will delete the others.
The process is repeated for every node of every table. To use the script to clear the database, execute the command:

     python psql_db_manager.py clear X

where X is an integer that specifies the maximum number of entries to keep for each node. If no X is specified, the default value used is 50.

NOTE: to execute the script (in both cases) you need to include the /monitor directory to the Python Path. To do that, execute the command:
     export PYTHONPATH=$PYTHONPATH:path_to_monitor_dir/monitor/   

'''
import sys
import psycopg2
from configuration import config

def get_connection(db=config.DB_NAME, host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD):
    try:
        connection_params = "dbname='{0}' user='{1}' host='{2}' password='{3}'".format(db, user, host, password)
        conn = psycopg2.connect(connection_params)
        return conn
    except:
        print "I am unable to connect to the database"

def execute_query(connection, query):    
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

def execute_operation(connection, operation):
    cursor = connection.cursor()
    cursor.execute(operation)
    cursor.execute("COMMIT")

def get_num_rows(connection, table):
    query = "SELECT count(*) FROM {0}".format(table)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0]


def exec_delete_duplicates(connection, table):
    #if table == 'clab_storage':
    if 'storage' in table:
        delete_duplicates_op = "SELECT * FROM delete_duplicates_storage('{0}')".format(table)
    else:
        delete_duplicates_op = "SELECT * FROM delete_duplicates('{0}')".format(table)
    cursor = connection.cursor()
    cursor.execute(delete_duplicates_op)
    #cursor.execute("COMMIT")
    
def exec_get_min_last_check(connection, table, max_entries_per_node):
    #if table == 'clab_storage':
    if 'storage' in table:
        get_min_last_check_op = "SELECT * FROM get_min_last_check_storage({0},'{1}')".format(max_entries_per_node, table)
    else:
        get_min_last_check_op = "SELECT * FROM get_min_last_check({0},'{1}')".format(max_entries_per_node, table)
    cursor = connection.cursor()
    cursor.execute(get_min_last_check_op)
    rows = cursor.fetchall()
    #cursor.execute("COMMIT")
    return rows
    
def exec_entries_per_node(connection, table, max_entries_per_node):
    #if table == 'clab_storage':
    if 'storage' in table:
        entries_per_node_op = "SELECT * FROM entries_per_node_storage({0},'{1}')".format(max_entries_per_node, table)
    else:
        entries_per_node_op = "SELECT * FROM entries_per_node({0},'{1}')".format(max_entries_per_node, table)
    cursor = connection.cursor()
    cursor.execute(entries_per_node_op)
    cursor.execute("COMMIT")

def delete_duplicates_database():
    connection = get_connection()
    for table in config.DB_TABLES:
        exec_delete_duplicates(connection, table)

def clear_database(max_entries_per_node=10):
    connection = get_connection()
    for table in config.DB_TABLES:
        exec_delete_duplicates(connection, table)
        exec_entries_per_node(connection, table, max_entries_per_node)


if __name__ == '__main__':
    operation = sys.argv[1] if len(sys.argv) > 1 else 'clear'
    max_entries_per_node = sys.argv[2] if len(sys.argv) > 2 else 50
    if operation == 'clear':
        clear_database(max_entries_per_node)
    elif operation == 'delete_duplicates':
        delete_duplicates_database()
    
    
    