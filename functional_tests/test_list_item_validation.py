from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

	# @skip
	def test_cannot_add_empty_list_items(self):
		# Edith goes to the home page and accidentally tries to submit an 
		# empty list item.  She hit Enter on the empty input box

		# The home page refreshes, and there is an error message 
		# saying that list items cannot be blank.

		# She tries again with some text for the item, which now works.

		# Perversely, she now decides to submit a second blank list item.

		# She receives a similar warning on the list page.

		# She can correct the error by filling in some text
		
		self.fail('This test has not yet been written!')