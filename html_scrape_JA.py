# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 12:00:42 2017

@author: jenna
"""

import requests
from bs4 import BeautifulSoup as bsoup

search_url = 'http://publicinterestlegal.org/county-list/'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}).content

parsed_html = bsoup(response, 'lxml')
target_rows = parsed_html.find_all('tr')

my_result_list = []
for row in target_rows:
    for x in row.find_all('td'):
        new_row = []
        for y in row.find_all('strong'):
            new_row.append(y.text.encode("ascii",'ignore'))
        
    my_result_list.append(new_row)
    
print 'jnerger'
print len(my_result_list)
print my_result_list

