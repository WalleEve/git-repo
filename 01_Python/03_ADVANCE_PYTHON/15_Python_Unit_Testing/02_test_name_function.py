# Unit Test and Test Case:

# A Passing Test 

import unittest 
from name_function import get_formatted_name 

class NamesTestCase(unittest.TestCase):
	""" Tests for name_function.py"""

	def test_first_last_name(self):
		"""Do names like 'Janis Joplin' works?"""
		formated_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formated_name, 'Janis Joplin')

unittest.main()

