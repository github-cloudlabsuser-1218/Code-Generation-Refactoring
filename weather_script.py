# fetch weather data from OpenWeatherMap API
import requests
def fetch_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        return weather_info
    else:
        return None
def display_weather(weather_info):
    if weather_info:
        print(f"Weather in {weather_info['city']}:")
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Description: {weather_info['description']}")
    else:
        print("Could not retrieve weather data. Please check the city name or API key.")
def main():
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter the city name: ")
    
    weather_info = fetch_weather(api_key, city)
    display_weather(weather_info)
if __name__ == "__main__":
    main()
# This code fetches weather data from the OpenWeatherMap API for a specified city.  
# It prompts the user for their API key and the city name, retrieves the weather data, and displays it in a user-friendly format.
# The code handles errors gracefully, informing the user if the data could not be retrieved.
# The `fetch_weather` function makes an API call to OpenWeatherMap, processes the response, and returns the weather information.
# The `display_weather` function formats and prints the weather information to the console.
# The `main` function orchestrates the user input and calls the other functions to fetch and display the weather data.
# The code is structured to be run as a standalone script, allowing users to easily check the weather for any city.
# The code is modular, with separate functions for fetching and displaying weather data, making it easy to maintain and extend.
# The code uses the `requests` library to handle HTTP requests, making it straightforward to interact with the OpenWeatherMap API.
# The code is written in Python, making it accessible to a wide range of users and developers.
# The code is designed to be user-friendly, with clear prompts for input and informative output.
# The code can be easily extended to include additional features, such as fetching forecasts or historical weather data.
