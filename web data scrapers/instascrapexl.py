# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 18:49:37 2021

@author: manik
"""

from bs4 import BeautifulSoup
import requests
import re
import xlsxwriter

classes=['10','9']
#subjects=['physics','chemistry','biology','maths']

subjects=['science','maths']
error_msg='The page you are looking for no longer exists. Perhaps you can return back to the homepage and see if you can find what you are looking for. Or, you can try finding it by using the search form below.'
       

for i in range(2):
    workbook = xlsxwriter.Workbook('class'+classes[i]+'.xlsx')
    for j in range(len(subjects)):    
        worksheet = workbook.add_worksheet(subjects[j])
        condt=True
        chapter_num=1
        row=0
        while(condt):
            html_text=requests.get('https://www.learninsta.com/class-'+classes[i]+'-'+subjects[j]+'-important-questions-chapter-'+str(chapter_num)+'/')
            chapter_num+=1
            
        
            soup = BeautifulSoup(html_text.text,'lxml')
            
            q1=soup.find(class_='entry-content')
            
            condt=not(q1.find('p').text==error_msg)
            print(q1.find('p').text==error_msg)
            
            
            for wrapper in q1.find_all('p'):
                if(wrapper.text==error_msg):
                    break
                worksheet.write(row,0,re.sub("Question|Answer","",wrapper.text))
                row+=1
        condt=True
        chapter_num=1
        print(row)
        while(condt):
            html_text=requests.get('https://www.learninsta.com/ncert-solutions-for-class-'+classes[i]+'-'+subjects[j]+'-chapter-'+str(chapter_num)+'/')
            chapter_num+=1
            
        
            soup = BeautifulSoup(html_text.text,'lxml')
            
            q1=soup.find(class_='entry-content')
            
            condt=not(q1.find('p').text==error_msg)
            print(q1.find('p').text==error_msg)
            
            #row=0
            for wrapper in q1.find_all('p'):
                if(wrapper.text==error_msg):
                    break
                worksheet.write(row,0,re.sub("Question|Answer","",wrapper.text))
                row+=1
                
    workbook.close()    


