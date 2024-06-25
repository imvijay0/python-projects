from flask import Flask,render_template,request 
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/weather')
def get_weather():
  city = request.args.get('city')

  #checking for empty strings and extra spaces
  if not bool(city.strip()):
    return render_template('city_not_found.html')

  weather_data = get_current_weather(city)

  # if city not found 
  if not weather_data['cod'] == 200:
    return render_template('city_not_found.html')

  tempInKelvin = weather_data["main"]["temp"]
  tempInCelsius = tempInKelvin - 273.15

  return render_template(
    "weather.html",
    title = weather_data["name"],
    status = weather_data["weather"][0]["description"].capitalize(),
    temp = f'{tempInCelsius:.1f}',  
    humidity = weather_data['main']['humidity'],
    
  )



if __name__ == '__main__':
  serve(app,host="0.0.0.0",port=8000)