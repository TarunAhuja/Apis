                                                                     
                                                                     
                                                                     
                                             
# -*- coding: cp1252 -*-

import nltk
import urllib2
from pprint import *;
import requests
import re
import json
import time
import amazonasinlinks as amazing
import wikipediaentityextractor as wikiped
import json
dict1={}
dict1['entities']={}
class Product:
    def productinfo(self, keyw):
        for i in keyw:
            print keyw
            dict1["entities"].update({i:{"name":0}})
            dict1["entities"][i].update({"freq":0})
            dict1["entities"][i].update({"product":0})
            dict1["entities"][i].update({"ASIN":0})
            dict1["entities"][i].update({"productinfo":0})
            dict1["entities"][i]["product"]=1
            dict1["entities"][i]["freq"]+=1
            j=i.replace(" ", '')
            j=j.upper()
            print "hey"
            ob=amazing.amazon13()
            asin=ob.amazon12(j)        
            dict1["entities"][i]["ASIN"]=asin
            a=wikiped.wikisoup()
            product_info=a.extract_infowiki(i)
            dict1["entities"][i]['productinfo']=product_info
        return json.dumps(dict1)    
##            except:
##                print " "
##            

