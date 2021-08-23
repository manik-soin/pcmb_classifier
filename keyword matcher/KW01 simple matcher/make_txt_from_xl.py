# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 16:49:00 2021

@author: manik

PREPARE .TXT FILE that contains the keywords
"""

import pandas as pd
import re
from nltk.corpus import stopwords
import pickle

def make_list_from_excel(filename,subjectname,keywords,badwords):
    df = pd.read_excel(filename, sheet_name=subjectname)#sheet names must be same as subject names 
    keywords[subjectname] = df[subjectname].tolist()#the first cell in excel must be subjectname
    print(subjectname+' Dictionary made...')
    print('Cleaning dictionary and removing stop words')
    keywords[subjectname] = [re.sub('[^A-Za-z0-9 ]+','',w.strip(',.').lower()) for w in keywords[subjectname]]
    keywords[subjectname]=' '.join(keywords[subjectname]).split()
    keywords[subjectname] = [word for word in keywords[subjectname] if not word in (stopwords.words() + badwords)]#remove stop words from nltk
    



def main():
    list_of_subjects=['Physics','Chemistry','Maths','Biology']
    keywords={}
    filename='pcmb_tags.xlsx'
    badwords=['due','two','problems','energy','problems','characteristics','uniformly','conservation']
    for subject in list_of_subjects:
        make_list_from_excel(filename,subject,keywords,badwords)
    print("Storing in a .txt pickle dump")
    with open("keyword_dictionary.txt", "wb") as fp:   #Pickling
        pickle.dump(keywords, fp)    
    print("New file saved.")

if __name__ == "__main__":
    main()
