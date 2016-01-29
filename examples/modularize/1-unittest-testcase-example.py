#!/usr/local/bin/python
# -*- coding: utf-8 -*-


import unittest
from selenium import webdriver

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
    	        print 'setUp: opening SAPO'
        self.driver.get('http://www.sapo.pt/')

    def test_search(self):
        input = self.driver.find_element_by_name('q')
        assert input.text == ''

    def test_another(self):
        assert self.driver.title == 'SAPO'

    def tearDown(self):
        print 'tearDown'

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()