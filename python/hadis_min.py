# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:35:54 2020

@author: merdi
"""






# import requests

# url = 'https://quranx.com/hadith/Bukhari/DarusSalam/Hadith-1/'
# res = requests.get(url)
# html_page = res.content
# # 



# from bs4 import BeautifulSoup

# soup = BeautifulSoup(html_page, 'html.parser')


# text = soup.find_all(text=True)

# output = ''
# blacklist = [
# 	"hadith-reference-list btn-group"
# 	# there may be more elements you don't want, such as "style", etc.
# ]

# for t in text:
# 	if t.parent.name in blacklist:
# 		output += '{} '.format(t)

# print(text)

# import urllib
# from bs4 import BeautifulSoup

# with urllib.request.urlopen("https://quranx.com/hadith/Bukhari/DarusSalam/Hadith-1/") as url:
#     html = url.read()
# soup = BeautifulSoup(html)

# # kill all script and style elements
# for script in soup(["script", "style"]):
#     script.extract()    # rip it out

# # get text
# text = soup.get_text()

# # break into lines and remove leading and trailing space on each
# lines = (line.strip() for line in text.splitlines())
# # break multi-headlines into a line each
# chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# # drop blank lines
# text = '\n'.join(chunk for chunk in chunks if chunk)

# print(text)
import numpy as np
import requests
from bs4 import BeautifulSoup

hadis = []
url = 'https://quranx.com/hadith/Bukhari/DarusSalam/Hadith-'
n_pages = 3

with open("file_min.txt", 'w', encoding='utf-8') as output:
    for i in range (1,n_pages+1):
        url_site = url+str(i)
        res = requests.get(url_site)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        result = soup.find_all("p", class_="highlightable")
        # text= "Dar-us-Salam reference Hadith"+str(i)
        
        for res in result:
                hadis = res.text
                
                print( hadis , file=output)
       
       

with open('file_min.txt', 'r',  encoding='utf-8') as file:
    data = file.read().replace('Narrated', '\nNarrated')
with open("hadis_min.txt", 'w', encoding='utf-8') as output:  
    print (data, file=output)
# print (data.replace ('Narrated', '\n\nNarrated'))
# list = np.array(data)

#\bidi@newrobustcmd\qurantext@i{% }
my_file = open("hadis_min.txt", encoding='utf-8')

hadis_clean = my_file.read()
# print(e)
sep = "Narrated"
for line in hadis_clean:
    result = [sep+x for x in hadis_clean.split(sep)]


#with open('hadus_final.txt', 'w',  encoding='utf-8') as h_f:
    for x in range(len(result)): 
        r=result[x]
        print('\\bidi@newrobustcmd\\qurantext@i{%% %s}' % r, file=h_f) 
#      idee definieren alpahbet als seperator und wenn zeichen nicht enthalten dann seperieren 





num_map = [(1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'), (100, 'c'), (90, 'xc'),
           (50, 'l'), (40, 'xl'), (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')]


def num2roman(num):

    roman = ''

    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i

    return roman

# test 




# for i in range(len(result)):
#     n=num2roman(i)
#     print('\\bidi@newrobustcmd\\qurantext@%s{%% }' % n)
#      for x in result:
#                 hadis = res.text
with open('hadus_final.txt', 'w',  encoding='utf-8') as h_f:
    for x in range(len(result)): 
        r=result[x]
        n=num2roman(x)
        print('\\bidi@newrobustcmd\\qurantext@%s{%% %s}' % (n,r), file=h_f) 


        





























