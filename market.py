from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")  # decorator
@app.route("/home")
def home_page():
    return render_template("home.html")


# navigation bar
