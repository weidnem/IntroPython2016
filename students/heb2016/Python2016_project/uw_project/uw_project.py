
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import sessionmaker

import psycopg2
import sys
import os
from os.path import join, dirname
from datetime import date, timedelta, datetime
from urllib import parse
from pandas   import DataFrame, ExcelWriter 
import pandas as pd

sql_dir = os.path.abspath('./sql')
 

## get sql
def dbconnection():

    msg_username=''
    msg_pass =''

    print('Please input your username:')
    msg_username = input().strip()
    print('Please input your password:')
    msg_pass = input().strip()
    host='host=gpdb.prod.cdk.com  dbname= fm01'
    username =str.join(' ', ('user=', msg_username))
    passwd = str.join(' ', ('password=', msg_pass))
    port = ' port = 5432' 

    def get_sql_source (sql_dir, sql_file_name):
        sql_loc = sql_dir + '/' + sql_file_name
        sql_source = ""
        sql_source = open(sql_loc).read()   
        return (sql_source) 
 
    for i in range (4):
        i=i+1
        sql_file_name = 'oem'+str(i)+'.sql'
        print(sql_dir, sql_file_name) 
        sql_source = get_sql_source(sql_dir,sql_file_name)  
        
        conn_string =str.join(' ', (host, username, passwd, port)) 

        connection = psycopg2.connect(conn_string)
        cursor = connection.cursor() 
        cursor.execute(sql_source)
        rescords = cursor.fetchall()
        connection.close()  

        if i==1:
            df1 =  DataFrame(rescords) 
            print('df1 total rows: ', len(df1))
            print(df1.head(2))
        if i==2:
            df2 =  DataFrame(rescords) 
            print('df2 total rows: ', len(df2)) 
        if i==3:
            df3 =  DataFrame(rescords)
            print('df3 total rows: ', len(df3)) 
        if i==4:
            df4 =  DataFrame(rescords)
            print('df4 total rows: ', len(df4)) 

    frames = [df1, df2, df3, df4]  
    result = pd.concat(frames)     
    print('Merged DataFrame Total Rows: ', len(result)) 
    print('resulult: ', result.head(2))
     
    row_counts= len(result)
    result_head=result.head(2)
    return (row_counts, result_head)

dbconnection()
