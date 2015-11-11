# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

import logging
import unittest

from keyvalueformatter import KeyValueFormatter
from six.moves import cStringIO


class LogTestCase(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger('logging-test')
        self.logger.setLevel(logging.DEBUG)
        self.buffer = cStringIO()

        self.logHandler = logging.StreamHandler(self.buffer)
        self.logHandler.setFormatter(KeyValueFormatter())
        self.logger.addHandler(self.logHandler)

    def test_default_format(self):
        '''Make sure the logger can take a simple string

        '''
        self.logger.info("a message")
        self.assertEqual(self.buffer.getvalue(),
                         'message="a message"\n')

    def test_dict_format(self):
        '''Make sure the logger can take a message within a dictionary

        '''
        self.logger.info(dict(
            message="a message"
        ))

        self.assertEqual(self.buffer.getvalue(),
                         'message="a message"\n')

    def test_dict_with_fields(self):
        '''Make sure the logger can handle complex types

        '''
        self.logger.info(dict(
            message="a message",
            field=True,
            more="More goes here",
            dict={'hello': 'world'},
            list=['nice', 'time'],
        ))

        if "u'" in self.buffer.getvalue():
            self.assertEqual(self.buffer.getvalue(),
                            '''dict="{u'hello': u'world'}"'''
                            ''';=field="True"'''
                            ''';list="[u'nice', u'time']"'''
                            ''';message="a message"'''
                            ''';more="More goes here"'''
                            '''\n''')
        else:
            self.assertEqual(self.buffer.getvalue(),
                            '''dict="{'hello': 'world'}"'''
                            ''';field="True"'''
                            ''';list="['nice', 'time']"'''
                            ''';message="a message"'''
                            ''';more="More goes here"'''
                            '''\n''')

if __name__ == '__main__':
    unittest.main()
