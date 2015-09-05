from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_a_cocktail_and_delete_it_later(self):
        # She access the cocktail list
        self.browser.get('http://localhost:8000/cocktails/')

        # She notices the page title and header mention cocktails
        self.assertIn('Cocktails', self.browser.title)
        self.fail('Finish the test!')

        # [...rest of comments as before]

if __name__ == '__main__':
    unittest.main(warnings='ignore')



# She access the cocktail list

# She logs in so that she can create a cocktail

# She goes to the cocktail creation page

# She types test-cocktail as name
# She types test description as description

# Then she creates one spirit ingredient (with data: 1 part of Rum)
# And goes to create mixer

# She creates a mixer (with data: 2 part of Coke) and clicks save

# As she likes the cocktail she just created she clicks on the favourite icon

# Finally, as this is just a test, she deletes the cocktail

# ------------------------------------------------------------------------------
# EXTRA
# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.