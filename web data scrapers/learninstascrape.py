# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 18:49:37 2021

@author: manik
"""

from bs4 import BeautifulSoup
import requests
import io
import openpyxl
 

error_msg='The page you are looking for no longer exists. Perhaps you can return back to the homepage and see if you can find what you are looking for. Or, you can try finding it by using the search form below.'
condt=True
chapter_num=1
while(condt):
    html_text=requests.get('https://www.learninsta.com/class-11-physics-important-questions-chapter-'+str(chapter_num)+'/')
    chapter_num+=1
    

    soup = BeautifulSoup(html_text.text,'lxml')
    
    q1=soup.find(class_='entry-content')
    
    condt=not(q1.find('p').text==error_msg)
    print(q1.find('p').text==error_msg)
    
    with io.open('physics.csv', 'a',encoding='utf-8') as fd:
            #csvwriter = csv.writer(csvfile)
        for wrapper in q1.find_all('p'):
            
            fd.write(wrapper.text)
            

    

# =============================================================================
# for wrapper in q1.find_all('p'):
#        print(wrapper.text)
#        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#        
# =============================================================================
