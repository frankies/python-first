# -*- coding: utf-8 -*-
__author__ = 'florije'


class ErrorWithArgs(Exception):
    def __init__(self, *args):
        # *args is used to get a list of the parameters passed in
        self.error_args = [a for a in args]


class NullException(Exception):
    pass


# try:
#     raise ErrorWithArgs(1, "text", "some more text")
# except ErrorWithArgs as e:
#     print "%d: %s - %s" % (e.error_args[0], e.error_args[1], e.error_args[2])
#     print e.message

try:
    raise NullException("1", "2")
except Exception as e:
    print e.message, e.args
