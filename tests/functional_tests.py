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

        # She sees that she needs to login in order to add a new cocktail
        login_button = self.browser.find_element_by_id('login')
        self.assertIn('Login', login_button.text)

        # She clicks the login button to go to the login page
        login_button.click()
        self.assertIn('Login', self.browser.title)

        # She fills the form with the login details and submits
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')

        username.send_keys('test_username')
        password.send_keys('test_password')

        self.browser.find_element_by_name('submit').click()

        # Once she is logged in she is redirected back to the cocktail list
        # Where she can now create a cocktail
        self.assertIn('Cocktails', self.browser.title)
        self.browser.find_element_by_link_text('Add new').click()

        # Now she needs to provide a name and description for the cocktail
        self.assertIn('Add cocktail', self.browser.title)

        title = self.browser.find_element_by_name('title')
        description = self.browser.find_element_by_name('description')

        title.send_keys('test_cocktail')
        description.send_keys('test_description')

        title.submit()

        # She is now taken to the add spirit screen, where she saves without
        # addding anything
        self.assertIn('Add spirit', self.browser.title)

        self.browser.find_element_by_link_text('Back to Cocktail').click()

        # She is now in the cocktail detail view, where she will finally
        # delete the cocktail
        self.assertIn('test_cocktail', self.browser.title)

        self.browser.find_element_by_link_text('Delete cocktail').click()
        self.browser.find_element_by_id('delete').click()



if __name__ == '__main__':
    unittest.main()



# Then she creates one spirit ingredient (with data: 1 part of Rum)
# And goes to create mixer

# She creates a mixer (with data: 2 part of Coke) and clicks save

# As she likes the cocktail she just created she clicks on the favourite icon


# ------------------------------------------------------------------------------
# EXTRA
# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.