import json
import urllib
from pprint import *;
import requests
import base64
import hmac
import urllib, urlparse
from  pprint import *
import requests
import time
import xmltodict, json
from lxml import etree
from hashlib import sha256 as sha256
import amazonproduct
import base64,hashlib,hmac,time
from urllib import urlencode, quote_plus
import re
class amazon13:
    def amazon12(self,item):
        config = {
        'access_key': 'AKIAJX42F6YYB4XMK6SQ',
        'secret_key': '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',
        'associate_tag': 'xataka-21',
        'locale': 'es'
            }
    
    
        params2={'AWSAccessKeyId':'AKIAJX42F6YYB4XMK6SQ',
             'AssociateTag':'xataka-21',
                 'Keywords':item,
            'Operation':'ItemSearch',
           'SearchIndex':'All',
            'Service':'AWSCommerceService',
         'Timestamp':time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()),
         'Version':'2010-09-01'
         
         
    }
        keys = params2.keys()
        keys.sort()
        values = map(params2.get, keys)
        url_string = urlencode(zip(keys,values))
        string_to_sign = "GET\necs.amazonaws.com\n/onca/xml\n%s" % url_string
        signature = hmac.new(
        key='bcU7Hqqiejh8SadQplHUgg0EkekOc9fLg1RLYPeP',
        msg=string_to_sign,
        digestmod=hashlib.sha256).digest()

        signature = base64.encodestring(signature).strip()
        urlencoded_signature = quote_plus(signature)
        url_string += "&Signature=%s" % urlencoded_signature
        base_url="http://ecs.amazonaws.com/onca/xml"
        service_url="%s?%s" % (base_url,url_string)
        api = amazonproduct.API(cfg=config)
        r=requests.get(service_url)
        o=xmltodict.parse(r.text)
        p=json.dumps(o)
        z=re.findall(r'[\'|"]ASIN[\'|"]{1}:[\s]?[\'|"]{1}(.+?)[\'|"]',p)
        z1=re.search(r'[\'|"]DetailPageURL[\'|"]{1}:[\s]?[\'|"]{1}(.+?)[\'|"]',p)
        try:
            return z[0]
            
        except:
            return None

        
    
    

