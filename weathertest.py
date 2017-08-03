import weather.py
# from weather.py import ConfNotFound, ConfNotValid
from weather.py import *
import unittest
import tempfile


class CheckUserConfig(unittest.TestCase):
    def test_check_config(self):
        """check_config should return true if there's valid user data and save
        it somewhere, else it should return false """
        self.assertRaises(ConfNotFound, weather.check_config(
            tempfile.gettempdir()))
        # How do I set up a temp file, with fake and real contents?
        with tempfile.NamedTemporaryFile() as f:
            self.assertRaises(ConfNotValid, weather.check_config(f))

        # Set up a file with valid contents here
        with tempfile.NamedTemporaryFile(mode='w+') as f:
            valid_contents = '1234'
            f.write(valid_contents)
            f.seek(0)
            self.assertTrue(weather.check_config(f))

    def test_get_user_config(self):
        """test requesting the user's config and writing it to a conf file"""

    def test_fetch_data(self):
        """test that data is fetched from the API"""

    def test_parse_data(self):
        """test that the function parses valid JSON from the API"""

    def test_construct_request_string(self):
        """test that this function constructs a string for the request that
        contains the needed info based on the parameters passed in"""
