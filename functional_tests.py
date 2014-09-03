from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):  # helper method
		table = self.browser.find_element_by_id('id_list_table')
		rows  = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])
		
	def test_can_start_a_list_and_retrieve_it_later (self):
		# checkout homepage for to-do app
		self.browser.get('http://localhost:8000')

		# notice the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# upon invite for to-do entry, user enters a to-do item: Buy apples
		# user enters a second to-do item, Make pie
		# at enter, page lists
		# 1: Buy apples
		# 2: Make pie
		# and an invite for to-do entry
		# and a unique url for user to-do list
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
		inputbox.send_keys('Buy apples')
		inputbox.send_keys(Keys.ENTER)

		self.check_for_row_in_list_table('1: Buy apples')

		# import time
		# time.sleep(10)

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Make pie')
		inputbox.send_keys(Keys.ENTER)
		self.check_for_row_in_list_table('1: Buy apples')
		self.check_for_row_in_list_table('2: Make pie')

		"""
		self.assertTrue(
			any(row.text == '1: Buy apples' for row in rows), "New to-do item did not appear in table -- its text was:\n%s" % (table.text,)
		)
		"""
		
		self.fail('Finish the test!')

		# user follows unique url and sees her list remembered
		# 1: Buy apples
		# 2: Make pie
		# and an invite for to-do entry
		# and a unique url for user to-do list

if __name__ == '__main__':
	unittest.main(warnings='ignore')