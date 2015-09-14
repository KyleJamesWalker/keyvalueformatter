# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

import logging
import unittest

import keyvalueformatter

from testfixtures import log_capture

try:
    from StringIO import StringIO
except ImportError:
    # Python 3 Support
    from io import StringIO


class LogTestCase(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger('logging-test')
        self.logger.setLevel(logging.DEBUG)
        self.buffer = StringIO()

        self.logHandler = logging.StreamHandler(self.buffer)
        self.logger.addHandler(self.logHandler)

    def test_default_format(self):
        fr = keyvalueformatter.KeyValueFormatter()
        self.logHandler.setFormatter(fr)

        self.logger.info("a message")
        log_value = self.buffer.getvalue()

        self.assetEqual(log_value, "msg='a message'")

    @log_capture()
    def test_log(self, l):
        self.logger.info('a message')
        self.logger.error('an error')

        l.check(
            ('root', 'INFO', "msg='a message'"),
            ('root', 'ERROR', "msg='an error'"),
        )

if __name__ == '__main__':
    # I need to look into this, not sure why it's not working
    # unittest.main()

    # For now just run a single manual test...
    logger = logging.getLogger('logging-test')
    logger.setLevel(logging.DEBUG)
    the_buffer = StringIO()

    logHandler = logging.StreamHandler(the_buffer)

    fr = keyvalueformatter.KeyValueFormatter(
        '%(levelname)s %(levelno)s %(pathname)s %(funcName)s'
        ' %(lineno)d %(exc_info)s %(message)s')
    logHandler.setFormatter(fr)
    logger.addHandler(logHandler)

    logger.info("a message")
    logger.info(dict(message="a message", fun=True))
    log_value = the_buffer.getvalue()
    print(log_value)
