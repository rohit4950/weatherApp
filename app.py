from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city_name = request.form['cityName']
        weather_data = get_weather(city_name)
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
