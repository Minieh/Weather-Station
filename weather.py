from flask import Flask, render_template
from sense_hat import SenseHat

app = Flask(__name__)

@app.route('/')

def index():
    sense = SenseHat()


    celcius = round(sense.get_temperature(), 1)
    fahrenheit = round(1.8 * celcius + 32, 1)
    humidity = round(sense.get_humidity(), 1)
    pressure = round(sense.get_pressure(), 1)

    return render_template('weather2.html', celcius=celcius, fahrenheit=fahrenheit, humidity=humidity, pressure=pressure)

    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
