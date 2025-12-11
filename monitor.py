from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route("/")
def index():
    ram = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)
    disk = psutil.disk_usage('/')

    data = {
        "ram_total": round(ram.total / (1024**3), 2),  # en Go
        "ram_utilisee": round(ram.used / (1024**3), 2),
        "ram_pourcent": ram.percent,
        "cpu_pourcent": cpu,
        "disk_total": round(disk.total / (1024**3), 2),
        "disk_utilise": round(disk.used / (1024**3), 2),
        "disk_pourcent": disk.percent
    }

    return render_template("index.html", data=data)