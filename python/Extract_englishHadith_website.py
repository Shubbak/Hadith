# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 17:42:07 2022

@author: merdi
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 17:23:29 2022

@author: merdi
"""
#import numpy as np

import requests
from bs4 import BeautifulSoup

hadis = []
url = 'https://quranx.com/hadith/Bukhari/DarusSalam/Hadith-'
n_pages = 20

with open("test_Website_arabisch_extract.txt", 'w', encoding='utf-8') as output:
    for i in range (1,n_pages+1):
        url_site = url+str(i)
        res = requests.get(url_site)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        result = soup.find_all("div", class_="hadith__text arabic")
        # text= "Dar-us-Salam reference Hadith"+str(i)
        
        for res in result:
                hadis = res.text
                
                print( hadis , file=output)