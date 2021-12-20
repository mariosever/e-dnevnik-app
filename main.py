from flask import Flask, render_template, request, make_response, redirect, url_for
from models import db, Ucenik

app = Flask(__name__)
db.create_all()


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(use_reloader=True)