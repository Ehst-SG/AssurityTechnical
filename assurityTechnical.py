# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:28:09 2022

@author: Seth Gunn
"""

# =============================================================================
# This program tests the api given at https://api.tmsandbox.co.nz/v1/Categories/6328/Details.json?catalogue=false,
# to the specifications:
# Name = "Badges"
# CanRelist = true
# The Promotions element with Name = "Feature" has a Description that contains the text "Better position in category"
# =============================================================================

import unittest
import requests

class testApi(unittest.TestCase):
    
    def setUp(self):
        # This function sets the web page that is to be tested and sends a request to it.
        page_url='https://api.tmsandbox.co.nz/v1/Categories/6328/Details.json?catalogue=false'
        response = requests.get(page_url)
        self.data = response.json()

    def testName(self):
        # This test checks that the value for "Name" is correct.
        self.assertEqual(self.data['Name'], 'Badges')

    def testRelist(self):
        # This test checks that the value for "CanRelist" is True.
        self.assertTrue(self.data['CanRelist'])

    def testFeature(self):
        # This test checks that the value for the element "Feature"'s description matches the correct value.
        s = "Better position in category"
        for item in self.data['Promotions']:
            if item['Name'] == 'Feature':
                self.assertEqual(item['Description'], s)


if __name__ == '__main__':
    unittest.main()