import weather.py
import unittest

class CheckUserConfig(unittest.TestCase):
    def test_find_config(self):
        """test if find_config can find the .weather file in the passed in
        directory"""

    def test_check_config(self):
        """check_config should return true if there's valid user data and save
        it somewhere, else it should return false """

    def test_get_user_config(self):
        """test requesting the user's config and writing it to a conf file"""

    def test_fetch_data(self):
        """test that data is fetched from the API"""

    def test_parse_data(self):
        """test that the function parses valid JSON from the API"""

    def test_construct_request_string(self):
        """test that this function constructs a string for the request that
        contains the needed info based on the parameters passed in"""
