# -*- coding: utf-8 -*-
"""
@author: Matthew Weidner

Read select a CSV files from the Metro website
Find the greatest and smallest time value in each file
output greatest and least time to a file.

"""

# import libraries
from urllib import request
import openpyxl


def get_route(route):
    # open connection
    response = request.urlopen("http://kingcounty.gov/~/media/depts/transportation/metro/data/schedules-sept-2016/a0{}.csv".format(route))
    
    # read and store contents
    csv = response.read()
    
    # decode to a str
    csvstr = str(bytes.decode(csv))
    
    # split str into rows
    lines = csvstr.split("\r\n")
    
    times = []
    hours = []
    # interrogate rows, elimiate first two and last line in file
    for line in lines[2:-1]:
        times.extend(line.split(",")[:-1]) #omit HTML in last column
    
    #clean list, isolate hours of service
    i = 0
    while i < len(times):
        try:
            hours.append(int(times[i][:times[i].find(':')])) #entries with valid times will have a ':'
            i += 1
        except:
            i += 1
            
            
    #find route's starting hour
    starthour = int(hours[0])
    
    #Find routes's last hour and convert to 28 hour service day
    if int(hours[-1]) < 5:
        endhour = int(hours[-1]) + 24
    else:
        endhour = int(hours[-1]) + 12
    return [starthour, endhour]

routes = {}

with open('routes.txt', 'r') as infile:
    for line in infile:
        
        rawroute = line[:3]

        if len(rawroute) == 3:
            routes[rawroute] = get_route(rawroute)
        else:
            pass

print(routes)
header = ['route','starthour','endhour']

wb = openpyxl.Workbook(write_only=True)
ws = wb.create_sheet(title="Routes")

ws.append(header)
for key, value in routes.items():
    ws.append([key,value[0],value[1]]) #write values



wb.save('RoutesMaxMin.xlsx')

#with open('routeMinMax.csv', 'wt', newline='') as outfile:
#    csvwrite = csv.writer(outfile, dialect='excel')
#    csvwrite.writerow(header) #create header row
#    for key, value in routes.items():
#        csvwrite.writerow([key,value[0],value[1]]) #write values
        
#f = open("historical.csv", "w")
#for line in lines:
#   f.write(line + "\n")
#f.close()