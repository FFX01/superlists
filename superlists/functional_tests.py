from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item',
        )
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

"""
user is invited to enter to do list item right away
"""

"""
User inputs 'Buy peacock feathers' into text box
"""

"""
User hits enter and page updates displaying '1: Buy peacock feathers as an
item in a to do list
"""

"""
There is still a text box prompting to add another list item. User enters
'Use peacock feathers to make a fly'
"""

"""
The page updates again and now both items are part of the list.
"""

"""
The user sees that the site will remember their list as there is a unique url
generated for them. There is text explaining this.
"""

"""
User visits their unique URL and their list is still there
"""

"""
User closes the browser.
"""