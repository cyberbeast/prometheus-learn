import urllib.request
import time
import names
import random
from terminaltables import SingleTable
import os
import click

click.clear()

table_data = [['Request','Response','Post Sleep Time']]
table = SingleTable(table_data)


for i in range(2000):
    sleep_tmr = random.randint(0,1)
    request = 'http://localhost:5000/hello/'
    response_ = ''
    click.clear()
    table_data.append([request, response_, sleep_tmr])
    print(table.table)
    with urllib.request.urlopen(request + names.get_first_name()) as response:
        response_ = str(response.read())
    
    click.clear()
    table_data[len(table_data)-1] = [request, response_, sleep_tmr]
    print(table.table)
    time.sleep(sleep_tmr)
    