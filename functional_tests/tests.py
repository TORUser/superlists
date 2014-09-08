from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

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
		self.browser.get(self.live_server_url)

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
		
		# IS Edith's url available?
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')


		# self.check_for_row_in_list_table('1: Buy apples')

		# import time
		# time.sleep(10)

		#  There is still a text box for adding more items, Edith adds: Make pie
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Make pie')
		inputbox.send_keys(Keys.ENTER) 
		
		# test input
		self.check_for_row_in_list_table('1: Buy apples')
		self.check_for_row_in_list_table('2: Make pie')

		"""
		self.assertTrue(
			any(row.text == '1: Buy apples' for row in rows), "New to-do item did not appear in table -- its text was:\n%s" % (table.text,)
		)
		"""

		# user follows unique url and sees her list remembered
		# 1: Buy apples
		# 2: Make pie
		# 3: Eat pie 
		# and a unique url for user to-do list
		
		## New browser session
		self.browser.quit()
		self.browser = webdriver.Firefox()

		# new user, Bobby should not see Edith's list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy apples', page_text)
		
		# Bobby starts new list
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy lettuce')
		inputbox.send_keys(Keys.ENTER)
		
		# Bobby gets his own url
		bobby_list_url = self.browser.current_url
		self.assertRegex(bobby_list_url, '/lists/.+')
		
		# Do Bobby and Edith have the SAME URL, they should not
		self.assertNotEqual(bobby_list_url, edith_list_url)
		
		# Satisfied, they go back to sleep

