from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later (self):
		# checkout homepage for to-do app
		self.browser.get('http://localhost:8000')

		# notice the page title and header mention to-do lists
		assert 'Django' in self.browser.title
		self.assertIn('To-Do', self.browser.title)
		self.fail("Finish the test!")

# upon invite for to-do entry, user enters a to-do item: Buy apples
# at enter, page lists:
# 1: Buy apples
# and an invite for to-do entry
# and a unique url for user to-do list

# user enters a second to-do item, Make pie
# at enter, page lists
# 1: Buy apples
# 2: Make pie
# and an invite for to-do entry
# and a unique url for user to-do list

# user follows unique url and sees her list
# 1: Buy apples
# 2: Make pie
# and an invite for to-do entry
# and a unique url for user to-do list

if __name__ == '__main__':
	unittest.main(warnings='ignore')