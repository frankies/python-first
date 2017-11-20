#!/usr/bin/env python
# encoding: utf-8

'''
中文
@author: mid0814
'''

from optparse import OptionParser 
import os
import sys

from springboot_const_vars import CONST_PJ_TYPE, CONST_LANG, CONST_PKG, CONST_JVM, \
    CONST_DEFAULT_GROUP, CONST_DEFAULT_ARTIFACT, CONST_DEFAULT_VERSION, log_msg
from springboot_creator_exec import  exec_zip_file_download


__all__ = []
__version__ = 0.1
__date__ = '2017-11-16'
__updated__ = '2017-11-16'

ARGS_DEBUG = 0
TESTRUN = 0
PROFILE = 0 
    
def main(argv=None):
    '''Command line options.'''

    program_name = os.path.basename(sys.argv[0])
    program_version = "v0.1"
    program_build_date = "%s" % __updated__

    program_version_string = '%%prog %s (%s)' % (program_version, program_build_date)
    program_longdesc = '''That's all, thanks!''' # optional - give further explanation about what the program does
    program_license = "Generate sprinboot skeleton by given feature                                            \
                Licensed under the Apache License 2.0\nhttp://www.apache.org/licenses/LICENSE-2.0"

    if argv is None:
        argv = sys.argv[1:]
    try:
        # setup option parser
        parser = OptionParser(usage="usage: %prog [options] <Group> <Artifact>",  
                              version=program_version_string, 
                              epilog=program_longdesc, 
                              description=program_license)
        
        parser.add_option("-t", 
                          "--project-type",  
                          dest="projectType", 
                          help="The project build method, \
                             eg. " + ",".join(CONST_PJ_TYPE) + ",\n default: %s" % "maven", 
                          type="choice", choices=CONST_PJ_TYPE  ,   
                          default="maven",
                          metavar="TYPE")
         
        parser.add_option("-l", 
                          "--lang",  
                          dest="lang", 
                          help="The programme language, eg." + ",".join(CONST_LANG) + ",\n default: %s" % "java", 
                          type="choice", choices=CONST_LANG,   
                          default="java",
                          metavar="LANGUAGE")
        
        parser.add_option("-r", 
                          "--springboot-version",
                          dest="springbootVersion", 
                          help="The version of springboot framework,\n default: 1.5.8.RELEASE", 
                          type="string",
                          default="1.5.8.RELEASE",
                          metavar="VERSION")
        
        parser.add_option("-p", 
                          "--packaging",
                          dest="packaging", 
                          help="The packaging type, eg."  + ",".join(CONST_PKG) + ",\n default: %s" % "jar",
                          type="choice", choices=CONST_PKG,   
                          default="jar",
                          metavar="PKG_TYPE")                   

        parser.add_option("-m", 
                          "--java-version",
                          dest="javaVersion", 
                          help="The jvm version, eg."  + ",".join(CONST_JVM) + ",\n default: %s" % "1.8"  ,
                          type="choice", choices=CONST_JVM,   
                          default="1.8",
                          metavar="JVM_VERSION")        
        
        parser.add_option("-d", 
                          "--dependencies",
                          dest="dependencies", 
                          help="*MUST IPUT*, The version of springboot framework, eg.web,jpa..." , 
                          type="string",
                          metavar="DEPENDENCIES") #2.0.0.M6, 1.5.8.RELEASE, 1.4.7.RELEASE

        parser.add_option("-o", 
                          "--output",
                          dest="output", 
                          help="The output directory, default: %s" %  os.getcwd(),
                          default= os.getcwd(),
                          metavar="OUTPUT_DIR")         

        parser.add_option("-g", 
                          "--prog",
                          dest="prog", 
                          help="The programme name",
                          default= program_name,
                          metavar="PROG_ID")
        # set defaults
#         parser.set_defaults(outfile="./out.txt", infile="./in.txt")

        # process options
        (opts, args) = parser.parse_args(argv)

        
        '''
            Preparing the parsed arguments
        ''' 
        dependencies = None
        if opts.dependencies is None: 
            fail_when_invalid_inputs("Dependencies must be input!", parser)
        else :
#             dependencies = opts.dependencies.split(',')
#             dependencies = map(lambda i: i.strip(), dependencies)
#             dependencies = filter(lambda i: len(i) >0, dependencies)
            dependencies = opts.dependencies
            del opts.dependencies
        
        # ....
        group = CONST_DEFAULT_GROUP
        artifact = CONST_DEFAULT_ARTIFACT
        version = CONST_DEFAULT_VERSION
        
        if len(args) > 0: 
            group = args[0]
            
        if len(args) > 1: 
            artifact = args[1]
            
        if len(args) > 2: 
            artifact = args[2]            
                
        log_msg("lang = %s" , str(opts)) 
        
        #Start....
        exec_zip_file_download(group, artifact, version, dependencies, opts)
        
        # MAIN BODY # 
    except Exception, e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2


def fail_when_invalid_inputs(msg, parser, code=1):
    sys.stderr.write("*** ERR: " + msg + 2 * "\n")
    parser.print_help(sys.stderr)
    
    sys.exit(code)
    
class IllegalInputs(Exception):
    
    def __init__(self, msg=None, stacktrace=None):
        self.msg = msg
        self.stacktrace = stacktrace
    
    def __str__(self):
        exception_msg = "Message: %s\n" % self.msg
        if self.stacktrace is not None:
            stacktrace = "\n".join(self.stacktrace)
            exception_msg += "Stacktrace:\n%s" % stacktrace
        return exception_msg     

if __name__ == "__main__":
    if ARGS_DEBUG:
        sys.argv.append("-h")
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'log_init_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())