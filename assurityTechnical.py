# -*- coding: utf-8 -*-
"""
@author: Seth Gunn
"""

# =============================================================================
# Write a procedure greedy_descent_with_random_restart(random_state, neighbours, cost) that takes three functions,
# one to get a new random state and two to compute the neighbours or cost of a state
# and then uses greedy_descent (you wrote earlier) to find a solution.
# The first state in the search must be obtained by calling the function random_state.
# The procedure must print each state it goes through (including the first and last one) in the order they are encountered.
# When the search reaches a local minimum that is not global, the procedure must print RESTART and restart the search by calling random_state
# =============================================================================


import unittest
import requests

class testApi(unittest.TestCase):
    
    def setUp(self):
        page_url='https://api.tmsandbox.co.nz/v1/Categories/6328/Details.json?catalogue=false'
        response = requests.get(page_url)
        self.data = response.json()

    def testName(self):
        self.assertEqual(self.data['Name'], 'Badges')

    def testRelist(self):
        self.assertTrue(self.data['CanRelist'])

    def testFeature(self):
        s = "Better position in category"
        for item in self.data['Promotions']:
            if item['Name'] == 'Feature':
                self.assertEqual(item['Description'], s)


if __name__ == '__main__':
    unittest.main()