#!/usr/bin/env/python3
"""
Process heat data for Isilon OneFS 7.2.1.3 generated using the following command:
isi statistics heat --pathdepth 3 --long --noheader --csv > clustername_ephochdate.csv

Labels for each row from heat file:
TimeStamp,Ops,Node,Event,Class,LIN,Path

InfluxDB line format for output file:
ops_per_sec,clusterName=<clusterName>,path=<myPath>,event=<myEvent> value=<myEventOps> <myDate>
ops_per_sec,clusterName=<clusterName>,node=<myNode> value=<myEventOps> <myDate>

curl -i -XPOST 'http://localhost:8086/write?db=mydb' --data-binary @cpu_data.txt
"""

import os

dict_path_iops = {}
dict_node_iops = {}
dict_total_iops = {}

file_list = []

def check_queues():

    quePaths = ['/Users/jbearer/scripts/misc/clus1/queued/', 
                '/Users/jbearer/scripts/misc/clus2/queued/']

    for paths in quePaths:
        fileName = os.listdir(paths)
        for file in fileName:
            file_list.append(paths + file)
    
    return file_list


if __name__ == '__main__':
    check_queues()

    print(file_list)
    # main()