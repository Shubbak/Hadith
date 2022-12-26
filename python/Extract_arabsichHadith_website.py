# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 17:23:29 2022

@author: merdi
"""
import numpy as np
import requests
from bs4 import BeautifulSoup
import time

list_of_hadis = []
url = 'https://quranx.com/hadith/Bukhari/DarusSalam/Hadith-'
start_page = 1
n_pages = 7563

with open("Website_arabisch_extract.txt", 'a', encoding='utf-8') as output:
    for i in range (start_page,n_pages+1):
        url_site = url+str(i)
        res = requests.get(url_site)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        result = soup.find_all("div", class_="hadith__text arabic")
        # text= "Dar-us-Salam reference Hadith"+str(i)
        list_of_hadis.append(result)
        
        for res in result:
                hadis = str(i) + res.text
                
                print( hadis , file=output)
        time.sleep(2)

    print("you appended {} ahadith.".format(len(list_of_hadis)), file=output)
