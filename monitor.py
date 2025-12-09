import platform
import psutil
import socket
import time
import os

machine = socket.gethostname()
exploitation = platform.system() + " " + platform.release()
uptime = int(time.time() - psutil.boot_time())
user = len(psutil.users())

coeur = os.cpu_count()
frequence = psutil.cpu_freq()
utilisation = psutil.cpu_percent(interval=1)

mem = psutil.virtual_memory()
totale = mem.total // (1024**3)
used = mem.used // (1024**3)
used1 = mem.percent

ip = socket.gethostbyname(machine)

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

print("result.html généré !")
