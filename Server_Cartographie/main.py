from flask import Flask, jsonify

from ConvertCSVtoGeoJSON import *

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify({'message': 'Hello, World!'})


# api qui retourne le geojson
@app.route('/geojson')
def geojson():
    return jsonify(ConvertCSVtoGeoJSON("dataset.csv")["data"])


if __name__ == '__main__':
    app.run(port=8000, debug=True)
