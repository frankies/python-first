 #!/usr/bin/env python
 # encoding: utf-8
 
import logconfig
import logging
 
logconfig.from_filename("log.yaml")
 
if __name__ == '__main__':
    
  l = logging.getLogger(__name__)
  l.debug("Hannnnlll- 有中文啦%s" % "heahaah")