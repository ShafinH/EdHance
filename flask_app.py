from flask import Flask, request, jsonify, render_template
from equations import equations
import pandas as pd


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# for more pages


@app.route('/eq/')
def rec():
    return render_template('index.html')


@app.route('/equation', methods=['POST'])
def eq():

    image = request.form['eq']

    output = equations.predict(image)

    return render_template('index.html', output)


@app.route('/essay', methods=['POST'])
def essay():

    essay = request.form['essay']

    output = essay.predict(essay)

    return render_template('index.html', output)


@app.route('/plag', methods=['POST'])
def plag():

    image = request.form['eq']

    output = plag.predict(image)

    return render_template('index.html', output)


if __name__ == "__main__":
    app.run(debug=True)
