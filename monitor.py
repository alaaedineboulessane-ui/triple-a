import platform
import psutil
import socket
import time
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    user_name = "Alice"
    return render_template("template.html", user_name=user_name)

app.run()
