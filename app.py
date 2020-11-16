from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    ## YOUR CODE HERE!!


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
