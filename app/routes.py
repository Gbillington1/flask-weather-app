import random
from app import app, geo
from flask import render_template, url_for, request, redirect, flash

@app.route('/')
def index():
    # location = geo.getLocation()
    # weather = geo.getCurrentWeather(location.latitude, location.longitude)
    # print(weather)
    return render_template('weather/index.html')

@app.route('/get-weather', methods=['POST'])
def get_weather():
    if request.method == 'POST':
        city=request.form['city']
        state=request.form['state']
        country=request.form['country']

        if not city:
            flash('Please enter a city.')
        elif not state:
            flash('Please enter a state.')
        elif not country:
            flash('Please enter a country.')
        else:
            location = geo.getLocation(city, state, country)
            weather = geo.getCurrentWeather(location.latitude, location.longitude)
            return render_template('weather/results.html', weather=weather)


# no idea where this came from
@app.route('/cats')
def cats():
    url = random.choice(cats)
    return render_template("cats.html", url=url)