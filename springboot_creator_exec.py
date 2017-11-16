#!/usr/bin/env python
# encoding: utf-8

'''
中文
@author: mid0814
'''

import os
from zipfile import ZipFile

import requests


CONST_SPRINGBOOT_INIT_URL = "https://start.spring.io/starter.zip"
# CONST_SPRINGBOOT_INIT_URL = "https://start.spring.io/starter.tgz"

def exec_zip_file_download(group, arti, deps, opts):
    
#         '''
#             type:maven-project
#             language:java
#             bootVersion:1.5.8.RELEASE
#             baseDir:demo
#             groupId:com.example
#             artifactId:demo
#             name:demo
#             description:Demo project for Spring Boot
#             packageName:com.example.demo
#             packaging:jar
#             javaVersion:1.8
#             autocomplete:
#             style:security
#             style:aop 
#         '''
    data = {
            
        "type": opts.projectType + "-project",
        "language": opts.lang,
        "bootVersion": opts.springbootVersion,
        "groupId": group,
        "artifactId": arti,
        "name": arti, 
         "baseDir": arti,
        "packageName": group,
        "description": "Generate by python..",
        "packaging": opts.packaging,
        "javaVersion": opts.javaVersion,
        "style": deps
    }
    
    res = requests.get(CONST_SPRINGBOOT_INIT_URL, data=data, stream=False)
    
    if res.status_code == 200:
        out_file_path = os.path.join(opts.output, arti + os.path.splitext(CONST_SPRINGBOOT_INIT_URL)[1])
        print "Response length: %d" % len(res.content) 
        with open(out_file_path, "wb") as f:
            f.write(res.content)
        
        #Extract files to this
#         import zipfile
#         
#         with ZipFile(out_file_path, 'r') as myzip:
#             myzip.extr
#     
#         z = zipfile.
#         z.extractall()
#         z.close()

#         import tarfile
#         tar = tarfile.open(out_file_path )
#         tar.extractall()
#         tar.close()
        
    else :
        raise Exception("Fail to download target file, status:%d, details: %s", res.status_code, res.content)
      
# url = "http://duckduckgo.com/html"
# payload = {'q':'python'}
# r = requests.post(url, payload)
# with open("requests_results.html", "w") as f:
#     f.write(r.content)
