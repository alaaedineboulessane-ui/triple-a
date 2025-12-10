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
frequence = psutil.cpu_freq().current
utilisation = psutil.cpu_percent(interval=1)

mem = psutil.virtual_memory()
totale = mem.total // (1024**3)
used = mem.used // (1024**3)
used1 = mem.percent

gour = list(psutil.process_iter(["pid", "name", "cpu_percent"]))

proc = []
for p in psutil.process_iter(['name']):
    try:
        p.cpu_percent(interval=None)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue

time.sleep(1)

for p in psutil.process_iter(['name']):
    try:
        cpu = p.cpu_percent(interval=None)
        proc.append([p.info['name'], [cpu]])
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue

def max_proc(liste):
    m = liste[0]
    for elem in liste:
        if elem[1][0] > m[1][0]:
            m = elem
    return m

def tri(liste):
    liste1 = []
    top = []
    while liste:
        m = max_proc(liste)
        liste1.append(m)
        liste.remove(m)
    for i in range(3):
        top.append(liste1[i])
    return top

l = tri(proc)
print(l)



ip = socket.gethostbyname(socket.gethostname())

with open("template.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("{{machine}}", machine)
html = html.replace("{{exploitation}}", exploitation)
html = html.replace("{{uptime}}", str(uptime))
html = html.replace("{{user}}", str(user))
html = html.replace("{{coeur}}", str(coeur))
html = html.replace("{{frequence}}", str(frequence))
html = html.replace("{{utilisation}}", str(utilisation) + "%")
html = html.replace("{{totale}}", str(totale) + "go")
html = html.replace("{{used}}", str(used) + "go")
html = html.replace("{{used1}}", str(used1) + "%")
html = html.replace("{{ip}}", ip)
html = html.replace("{{gourmand}}", str(l[0]) + "  " + str(l[1]) + "  " +str(l[2]))


with open("result.html", "w", encoding="utf-8") as f:
    f.write(html)


