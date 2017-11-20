#!/usr/bin/env python
# encoding: utf-8

'''
    If you click on "Generate Project" on the web ui of our instance, it will download a project archive with a Maven-based project and the necessary infrastructure to start a basic Spring Boot app.
    
    You could achieve the same result with a simple curl command
    
    $ curl https://start.spring.io/starter.zip -o demo.zip
    The web ui exposes a bunch of options that you can configure. These are mapped to the following request attributes:
    
    Basic information for the generated project: groupId, artifactId, version, name, description and packageName
    
    The name attribute is also used to generate a default application name. The logic is that the name of the application is equal to the name attribute with an Application suffix (unless said suffix is already present). Of course, if the specified name contains an invalid character for a java identifier, Application is used as fallback.
    
    The artifactId attribute not only defines the identifier of the project in the build but also the name of the generated archive.
    
    dependencies (or style): the identifiers of the dependencies to add to the project. Such identifiers are defined through configuration and are exposed in the metadata.
    
    type: the kind of project to generate (e.g. maven-project). Again, each service exposes an arbitrary number of supported types and these are available in the metadata.
    
    javaVersion: the language level (e.g. 1.8).
    
    bootVersion: the Spring Boot version to use (e.g. 1.2.0.RELEASE).
    
    language: the programming language to use (e.g. java).
    
    packaging: the packaging of the project (e.g. jar).
    
    applicationName: the name of the application class (inferred by the name attribute by default).
    
    baseDir: the name of the base directory to create in the archive. By default, the project is stored in the root.
    
    This command generates an another-project directory holding a Gradle web-based Groovy project using the actuator:
    
    $ curl https://start.spring.io/starter.tgz -d dependencies=web,actuator \
    -d language=groovy -d type=gradle-project -d baseDir=another-project | tar -xzvf -
    Note
    The /starter.tgz endpoint offers the same feature as /starter.zip but generates a compressed tarball instead.
    You could use this infrastructure to create your own client since the project is generated via a plain HTTP call.
    
'''
'''
中文
@author: mid0814
'''
# CONST_SPRINGBOOT_INIT_URL = "http://localhost:89"

import os
from zipfile import ZipFile

import requests

from springboot_const_vars import CONST_SPRINGBOOT_INIT_URL, log_msg


def exec_zip_file_download(group, arti, version, deps, opts):
    
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
        "version": "1.0",
        "name": arti, 
         "baseDir": arti,
        "packageName": group,
        "description": "Generate by python..",
        "packaging": opts.packaging,
        "javaVersion": opts.javaVersion,
#         "style": deps,
        "dependencies": deps
    }
    
    res = requests.post(CONST_SPRINGBOOT_INIT_URL, data=data, stream=False)
    
    if res.status_code == 200:
        if not os.path.isdir(opts.output):
            os.makedirs(opts.output)
        
        import tempfile
        out_file_path = os.path.join(tempfile.gettempdir(), arti + os.path.splitext(CONST_SPRINGBOOT_INIT_URL)[1])
        log_msg("Response length: %d" % len(res.content)) 
        with open(out_file_path, "wb") as f:
            f.write(res.content)
        
        extract_tar(out_file_path, opts.output)
            

    else :
        raise Exception("Fail to download target file, status:%d, details: %s" % (res.status_code , res.content) )

'''
Extract tar to directory and delete it at last.
'''
def extract_tar(srcPath, extractTargetDir): 
    
    ##Extract...
    if not os.path.isdir(extractTargetDir):
        os.makedirs(extractTargetDir)    
        
    import tarfile
    tar = tarfile.open(srcPath)
    tar.extractall(extractTargetDir)
    tar.close()
    
    #Delete .tgz.
    log_msg("tmp path:%s" % srcPath)
    
    try:
        os.remove(srcPath)
        assert not os.path.isfile(srcPath)
    except OSError, e:  ## if failed, report it back to the user ##
        log_msg ("Error: %s - %s." % (e.filename,e.strerror))
        raise  
    
# def extract_zip():
  #Extract files to this
#         import zipfile
#         
#         with ZipFile(out_file_path, 'r') as myzip:
#             myzip.extr
#     
#         z = zipfile.
#         z.extractall()
#         z.close()      
# url = "http://duckduckgo.com/html"
# payload = {'q':'python'}
# r = requests.post(url, payload)
# with open("requests_results.html", "w") as f:
#     f.write(r.content)
