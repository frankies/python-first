# -*- coding: utf-8 -*-
__author__ = 'florije'

import logging


# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def foo():
    logger.warn('Hi, foo')


class Bar(object):
    def bar(self):
        logger.warn('Hi, bar')


# def foo():
#     logger = logging.getLogger(__name__)
#     logger.info('Hi, foo')
#
#
# class Bar(object):
#     def __init__(self, logger=None):
#         self.logger = logger or logging.getLogger(__name__)
#
#     def bar(self):
#         self.logger.info('Hi, bar')


if __name__ == '__main__':
    foo()
    bar_instance = Bar()
    bar_instance.bar()
