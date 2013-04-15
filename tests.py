#!flask/bin/python

import unittest
from app import app


class AppTestSuite(unittest.TestCase):

    def setUp(self):
        #Your init code here
        app.config.from_object('config.TestingConfig')

    def test_basic(self):
        #This is a sample test that returns true
        self.assertEqual(1+1, 2)

    def tearDown(self):
        #Your cleanup code here
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppTestSuite)
    unittest.TextTestRunner(verbosity=2).run(suite)
