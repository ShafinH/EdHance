from flask import Flask, request, jsonify, render_template
from equations import equations
import pandas as pd


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# for more pages


@app.route('/equation/')
def rec():
    return render_template('index.html')


@app.route('/equation', methods=['POST'])
def eq():

    image = request.form['eq']

    answer = equations.predict(image)

    return render_template('index.html', answer)


@app.route('/essay', methods=['POST'])
def essay():

    essay = request.form['essay']

    grade = essay.predict(essay)

    return render_template('index.html', grade)


@app.route('/plag', methods=['POST'])
def plag():

    image = request.form['eq']

    plagiarism = plag.predict(image)

    return render_template('index.html', plagiarism)


if __name__ == "__main__":
    app.run(debug=True)
