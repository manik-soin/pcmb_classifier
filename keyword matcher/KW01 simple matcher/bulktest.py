# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:39:13 2021

@author: manik
"""

import pickle
import pandas as pd
def keyword_matcher(test_string,keywords):
    matches={}
    for key in keywords.keys():
       matches[key] = [ele for ele in keywords[key] if((' ' + ele + ' ') in (' ' + test_string + ' '))]

    max_key = max(matches, key= lambda x: len(set(matches[x]))) 

    total_matches=0
    for key in matches.keys():
        total_matches+=len(matches[key])
    
    
    
    if(total_matches==0):
        return 'zero_matches'
    else:    
        return max_key
        
def prepare_questions(filename,list_of_subjects,questions):
    for subjectname in list_of_subjects:
        df = pd.read_excel(filename, sheet_name=subjectname)
        questions[subjectname] = df[subjectname].tolist()       
        questions[subjectname] = [x for x in questions[subjectname] if not isinstance(x, int)]       
            
def main():
    with open("keyword_dictionary.txt", "rb") as fp:   # Unpickling
        keywords = pickle.load(fp)
    
    list_of_subjects=keywords.keys()
    filename='test_dataset.xlsx'
    questions={}
    prepare_questions(filename,list_of_subjects,questions)
    for subjectname in list_of_subjects:
        print(filename.upper()+" "+subjectname.upper()+" QUESTION DATABASE TEST")
        result_dict={}
        result_dict['zero_matches']=0
        for s in list_of_subjects:
            result_dict[s]=0
        for question in questions[subjectname]:
            result=keyword_matcher(question,keywords)
            result_dict[result]+=1
        total_strings=len(questions[subjectname])
        print("Accuracy: "+str((result_dict[subjectname]/total_strings)*100)+"%")
        print("\nNumber of questions correctly identified= ",result_dict[subjectname])
        print("Total tests conducted=",total_strings)
        
        print("\nNumber of Zero Match cases= ",result_dict['zero_matches'])
        print("Accuracy removing zero match cases: "+str((result_dict[subjectname]/(total_strings-result_dict['zero_matches'])*100))+"%")
        print('\n-----------------------------------------------------------------\n')
            
    
    


if __name__ == "__main__":
    main()