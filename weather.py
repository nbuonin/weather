def find_config():
    ```Check the passed in directory for a file named .weather
    If it does return a pointer to the file, if not return None```

def check_config():
    ``` This function checks if there's a config file. If there's one it loads
    in the API key and default zipcode. If not, it asks the user for a key and
    a default zipcode.

   returns a two element list or None on fail```

def get_user_config(directory):
    ``` get the API key and a default zipcode from the user, and save it
    inside the directory passed in```

def fetch_data():
    ``` request data from API and print out requested forecast ```

def parse_data():
    ```parse the JSON feed and return a string```

def construct_request_string():
    ```construct request string for request based on the parameters passed in.
    These include:
        - zipcode
        - current weather
        - hourly forecast
        - five day forcast

    Returns a string
    ```
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
        ``` and do it all over again```
    else:
        request = construct_request_string(```with all the args```)
        weather_json = fetch_data(request)
        print(parse_data(weather_json))
        return
