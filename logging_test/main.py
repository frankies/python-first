#!/usr/bin/env python
# encoding: utf-8

__author__ = 'florije'

import logging
import logging.config

# load my module

import my_module

class MyException(Exception):

    """A base class for CherryPy exceptions."""
    pass

class Test(object):
    
    def __init__(self, count=0):
        self.count = count
        self.log = logging.getLogger("Test")
        
    def increase(self):
        self.count= self.count + 1
        return self
        
    def printMe(self):
      self.log.warn(self.count)
      try:
          raise MyException()
      except Exception as  e:  
          self.log.error("error detail: %s" % "TEST" )
      finally:
          self.log.info("bye!")
      
      
# load the logging configuration


logging_config = dict(
    version=1,
    disable_existing_loggers=False,
    formatters={
        'format': {'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
    },
    handlers={
        'sh': {'class': 'logging.StreamHandler',
               'formatter': 'format',
               'level': logging.DEBUG},
        'fh': {
            'class': 'logging.FileHandler',
            'formatter': 'format',
            'level': logging.DEBUG,
            'filename': "py.log" 
        }
    },
    loggers={
        '': {'handlers': ['fh'],
             'level': logging.WARN}
    }
)

another_config = {
    'version': 1,
    'disable_existing_loggers': False,  # this fixes the problem

    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s]  %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
#        'rfh': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': 'logconfig.log',
#             'backupCount': 3,
#             'maxBytes': 10 
#         },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

# logging.config.dictConfig(another_config)
logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    
    t = Test()
    t.increase()
    t.printMe()
    
    logger.info('start.') 
    my_module.foo()
    bar = my_module.Bar()
    bar.bar() 
    logger.info('end.')
    
