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
    unittest.main()
