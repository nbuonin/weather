def check_config(home_directory):
    """ This function checks if there's a config file. If there's one it loads
    in the API key and default zipcode. If not, it asks the user for a key and
    a default zipcode

    my plan for this is to check for the config file. If the file is missing
    it should throw a 'ConfNotFount' exception, and handle it by asking the
    user for the info, or canceling out.
    If it finds the conf file, but its not valid, it should throw a
    'ConfNotValid' exception and ask the user for the info
   returns a two element list or None on fail"""


def request_user_config(directory):
    """ request the API key and a default zipcode from the user, and save it
    inside the directory passed in"""


def fetch_data():
    """ request data from API and print out requested forecast """


def parse_data():
    """parse the JSON feed and return a string"""


def construct_request_string():
    """construct request string for request based on the parameters passed in.
    These include:
        - zipcode
        - current weather
        - hourly forecast
        - five day forcast

    Returns a string
    """


class ConfNotFound(Exception):
    def __init__(self):
        self.message = "The configuration file can't be found"


class ConfNotValid(Exception):
    def __init__(self):
        self.message = "The configuration file isn't valid"


if __name__ == '__main__':
    print("Hello World")

    conf_file = find_config('~/')
    conf = []
    if (conf_file):
        conf = check_config(conf_file)
    else:
        get_user_config('~/')

    if (conf.length != 2):
        get_user_config('~/')
        """ and do it all over again"""
    else:
        request = construct_request_string("""with all the args""")
        weather_json = fetch_data(request)
        print(parse_data(weather_json))
        return
