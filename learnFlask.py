from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("html.html", title="name")


@app.route("/dat")
def name():
    return render_template("children.html", title="name")


if __name__ == "__main__":
    app.run(debug=True)
