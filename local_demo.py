# -*- coding: utf-8 -*-
__author__ = 'florije'

import simplejson
import logging

if __name__ == '__main__':
    simple_dict = {"name": "florije", 'age': 20}
    
    simple_json = simplejson.dumps(simple_dict)
    print simple_json
