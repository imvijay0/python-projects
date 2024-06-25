from dotenv import load_dotenv
from pprint import pprint
import os
import requests

# load .env file to the environment. (laoding all the variables)
load_dotenv()

def get_current_weather(city="hyderabad"):

  request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}'

  weather_data = requests.get(request_url).json()
  return weather_data

if __name__ == "__main__":
  # print('\n Get current weather conditions\n')

  city = input('\n Please enter a city name')

  weather_data = get_current_weather(city)

  # print('\n')
  # pprint(weather_data)



