import platform
import psutil
import socket
import time
import os
from flask import Flask, render_template

machine = socket.gethostname()
exploitation = platform.system() + " " + platform.release()
uptime = int(time.time() - psutil.boot_time())
user = len(psutil.users())

coeur = os.cpu_count()
frequence = psutil.cpu_freq().current
utilisation = psutil.cpu_percent(interval=1)

mem = psutil.virtual_memory()
totale = mem.total // (1024**3)
used = mem.used // (1024**3)
used1 = mem.percent

gour = list(psutil.process_iter(["pid", "name", "cpu_percent"]))


def tri3(liste):
    proc = []
    for p in psutil.process_iter(['name', 'cpu_percent']):
        proc.append([p.info['name'],[p.info["cpu_percent"]]])
    copie = []
    for i in range(3):
        if proc[i-1][1] > proc[i][1]:
            copie.append(proc[i][1])
    return copie

print(tri3(gour))

ip = socket.gethostbyname(socket.gethostname())

with open("template.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("{{machine}}", machine)
html = html.replace("{{exploitation}}", exploitation)
html = html.replace("{{uptime}}", str(uptime))
html = html.replace("{{user}}", str(user))
html = html.replace("{{coeur}}", str(coeur))
html = html.replace("{{frequence}}", str(frequence))
html = html.replace("{{utilisation}}", str(utilisation))
html = html.replace("{{totale}}", str(totale))
html = html.replace("{{used}}", str(used))
html = html.replace("{{used1}}", str(used1))
html = html.replace("{{ip}}", ip)


with open("result.html", "w", encoding="utf-8") as f:
    f.write(html)

@app.route("/")
def home():
    user_name = "Alice"
    return render_template("template.html", user_name=user_name)

app.run()
