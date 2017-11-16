import argparse
import os
import sys
 

__all__ = []
__version__ = 0.1
__date__ = '2017-11-16'
__updated__ = '2017-11-16'

program_name = os.path.basename(sys.argv[0])
program_version = "v0.1"
program_build_date = "%s" % __updated__

program_version_string = '%%prog %s (%s)' % (program_version, program_build_date)
program_longdesc = '''That's all, thanks!''' # optional - give further explanation about what the program does
program_license = "Copyright 2017 mid0814 (ymslx)                                            \
            Licensed under the Apache License 2.0\nhttp://www.apache.org/licenses/LICENSE-2.0"


parser = argparse.ArgumentParser(version=program_version_string, epilog=program_longdesc, description=program_license)
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print args.accumulate(args.integers)