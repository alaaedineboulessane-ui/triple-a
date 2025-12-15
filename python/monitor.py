import platform
import psutil
import socket
import time
import os

machine = socket.gethostname()
exploitation = platform.system() + " " + platform.release()
uptime = int(time.time() - psutil.boot_time()) // 60
user = len(psutil.users())

coeur = os.cpu_count()
frequence = psutil.cpu_freq().current

load1 = psutil.cpu_percent(interval=1)
load5 = psutil.cpu_percent(interval=5)
load15 = psutil.cpu_percent(interval=15)
cpu_per_core = psutil.cpu_percent(interval=1, percpu=True)

mem = psutil.virtual_memory()
totale = mem.total // (1024**3)
used = mem.used // (1024**3)
used1 = mem.percent

disk = psutil.disk_usage('/')
disk_total = disk.total // (1024**3)
disk_used = disk.used // (1024**3)
disk_percent = disk.percent

proc = []
for p in psutil.process_iter(['name']):
    try:
        cpu = p.cpu_percent(interval=None)
        proc.append([p.info['name'], cpu])
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue

time.sleep(1)
for p in psutil.process_iter(['name']):
    try:
        cpu = p.cpu_percent(interval=None)
        proc.append([p.info['name'], cpu])
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue

top_proc = sorted(proc, key=lambda x: x[1], reverse=True)[:3]

EXTENSIONS = [".txt",".pdf",".jpg",".webp",".ahk",".url",".docx",".png",".mp4",".csv"]

def compte(dossier):
    stats = {ext:0 for ext in EXTENSIONS}
    stats["dossier"] = 0
    largest_files = []
    for root, dirs, files in os.walk(dossier):
        stats["dossier"] += len(dirs)
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            path = os.path.join(root, file)
            if ext in stats:
                stats[ext] += 1
            largest_files.append((path, os.path.getsize(path)))
    largest_files.sort(key=lambda x: x[1], reverse=True)
    return stats, largest_files[:5]

analyse_stats, largest_files = compte("C:/Users/aladi/OneDrive/Bureau/Documents")

def pourcent(stats):
    total = sum(stats.values())
    return {k: round(v/total*100) for k,v in stats.items()}

ip = socket.gethostbyname(socket.gethostname())

with open("html/template.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("<head>", "<head>\n<meta http-equiv='refresh' content='30'>")
html = html.replace("{{machine}}", machine)
html = html.replace("{{exploitation}}", exploitation)
html = html.replace("{{uptime}}", str(uptime) + " minutes")
html = html.replace("{{user}}", str(user))
html = html.replace("{{coeur}}", str(coeur))
html = html.replace("{{frequence}}", f"{frequence:.2f} MHz")

html = html.replace("{{utilisation}}", '\n'.join(
    f"<div class='gauge'><div class='fill' style='width:{u}%; background-color:{'green' if u<=50 else 'orange' if u<=80 else 'red'}'></div><span>{u}%</span></div>" 
    for u in cpu_per_core
))

html = html.replace("{{loadavg}}", f"{load1}%, {load5}%, {load15}%")

html = html.replace("{{totale}}", str(totale) + " Go")
html = html.replace("{{used}}", str(used) + " Go")
html = html.replace("{{used1}}", f"<div class='gauge'><div class='fill' style='width:{used1}%; background-color:{'green' if used1<=50 else 'orange' if used1<=80 else 'red'}'></div><span>{used1}%</span></div>")

html = html.replace("{{disk_total}}", str(disk_total) + " Go")
html = html.replace("{{disk_used}}", str(disk_used) + " Go")
html = html.replace("{{disk_percent}}", f"<div class='gauge'><div class='fill' style='width:{disk_percent}%; background-color:{'green' if disk_percent<=50 else 'orange' if disk_percent<=80 else 'red'}'></div><span>{disk_percent}%</span></div>")

html = html.replace("{{ip}}", ip)
html = html.replace("{{gourmand}}", '<br>'.join([f"{p[0]} : {p[1]}%" for p in top_proc]))
html = html.replace("{{analyse}}", '<br>'.join([f"{k}: {v}%" for k,v in pourcent(analyse_stats).items()]))
html = html.replace("{{largest_files}}", '<br>'.join([f"{f[0]} ({f[1]//1024} KB)" for f in largest_files]))

with open("html/result.html", "w", encoding="utf-8") as f:
    f.write(html)
