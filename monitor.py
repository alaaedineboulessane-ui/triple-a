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



def tipe(objet):
    return os.path.splitext(objet)[1].lower()



txt = 0
pdf = 0
jpg = 0
webp = 0
ahk = 0
url = 0
docx = 0
unknown = 0
doss = 0

def compte(dossier):
    l = [0,0,0,0,0,0,0,0]
    for item in os.listdir(dossier):
        chemin_complet = os.path.join(dossier, item)
        if os.path.isfile(chemin_complet):
            if tipe(item) == ".txt":
                l[0] += 1
            elif tipe(item) == ".pdf":
                l[1] += 1
            elif tipe(item) == ".jpg":
                l[2] += 1
            elif tipe(item) == ".webp":
                l[3] += 1 
            elif tipe(item) == ".ahk":
                l[4] += 1
            elif tipe(item) == ".url":
                l[5] += 1
            elif tipe(item) == ".docx":
                l[6] +=1
        elif os.path.isdir(chemin_complet):
            l[7] += 1
    return l

def pourcent(liste):
    taille = len(liste)
    total = 0
    for i in range(taille):
        total += liste[i]
    pourcent_txt = round(liste[0] / total * 100)
    pourcent_pdf = round(liste[1] / total * 100)
    pourcent_jpg = round(liste[2] / total * 100)
    pourcent_wepb = round(liste[3] / total * 100)
    pourcent_ahk = round(liste[4] / total * 100)
    pourcent_url = round(liste[5] / total * 100)
    pourcent_docx = round(liste[6] / total * 100)
    pourcent_dossier = round(liste[7] / total * 100)
    return [pourcent_txt, pourcent_pdf, pourcent_jpg,pourcent_wepb, pourcent_ahk, pourcent_url, pourcent_docx, pourcent_dossier] 

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
html = html.replace("{{analyse}}", str(pourcent(compte("C:/Users/aladi/OneDrive/Bureau/Documents"))))


with open("result.html", "w", encoding="utf-8") as f:
    f.write(html)


