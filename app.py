from flask import Flask, request, render_template, url_for, flash
import os
import datetime

UPLOAD_FOLDER = '/tmp/'
app = Flask(__name__)
app.secret_key = 'some secret key'

@app.route("/")
def index():
    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)