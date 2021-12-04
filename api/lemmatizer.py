#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Lemmatizer class

Created: 2021 12 04
Author: lukasp
Based on code by Andrius Utka
"""

import requests
import json
import re
import os

LEX = "http://"+os.getenv("LEX", "my-semantika-lex")+":8080"     #"http://localhost:1123"
MORPH = "http://"+os.getenv("MORPH", "my-semantika-morph")+":8090/morphology" #"http://localhost:1122"

class Lemmatizer:
    """Lemmatizer Class to lemmatize and annotate Lithuanian text"""
    
    def __init__(self, LEX, MORPH):
        self.LEX = LEX
        self.MORPH = MORPH
        
    def pre_process(self, text:str)->str:
        """
        Pre-process text by removing extra 
        spaces and newline characters
        """
        text = re.sub("\s+\n","\n", text)
        text = re.sub("\n+","\n", text)
        return text
    
    def split_into_sentences(self, text:str)->list:
        """Splits text into a list of sentences"""
        text_utf = text.encode()
        response = requests.post(self.LEX, data=text_utf)
        lex_dict = json.loads(response.content.decode("utf8"))

        lex_dic_sent = lex_dict['s']
        sentence_list=[]
        for s in lex_dic_sent:
            begin = s[0]
            length = s[1]
            end = begin+length
            sentence = text[begin:end]
            sentence_list.append(sentence)
        return sentence_list
    
    def tokenize(self,sentence_list:list)->list:
        """
        Converts a list of sentences into 
        a list of word tokens
        """
        self.text = ""
        for line in sentence_list:
            self.text += line + " " +"<s>" + " "

        text_utf = self.text.encode("utf8")
        response = requests.post(self.LEX, data = text_utf)
        self.token_response = response.content.decode("utf8")
        lex_dict = json.loads(response.content.decode("utf8"))
        lex_dict_tokens = lex_dict['seg']

        self.token_list=[]
        for item in lex_dict_tokens:
            begin = item[0]
            length = item[1]
            end = begin+length
            token = self.text[begin:end]
            self.token_list.append(token)

    def lemmatize(self):
        """Lemmatizes tokens"""
        proc_text = re.sub("\"","\\\"",self.text)
        message_body = "{\"body\":\"" + proc_text + "\",\"annotations\":{\"lex\":" + self.token_response + "}}"
        message_body_utf = message_body.encode()
        headers = {'Content-type': 'application/json'}
        response = requests.post(self.MORPH, data= message_body_utf, headers=headers)
        response_proc = json.loads(response.text)
        msd_dict = response_proc['msd']
        
        self.final_results = []
        for index, item in enumerate(self.token_list):
            list1 = msd_dict[index]
            list2 = list1[0]
            lema = list2[0]
            morf = list2[1]
            d = {"original" : item, "lemma" : lema, "morph" : morf}
            self.final_results.append(d)

    def lemmatize_text(self, text):
        """Main function to lemmatize text"""
        proc_text = self.pre_process(text)
        sentences = self.split_into_sentences(proc_text)
        self.tokenize(sentences)
        self.lemmatize()
        return self.final_results