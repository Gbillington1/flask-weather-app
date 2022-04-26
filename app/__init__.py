from flask import Flask
import os

# workaround for a geopy SSL error
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
from app.static.cats import cats
from app import routes

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
