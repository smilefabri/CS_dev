import psutil

"""
install lib = pip install psutil.

psutil (process and system utilities)
è una libreria multipiattaforma per recuperare informazioni sui processi in esecuzione e sull'utilizzo del sistema 
(CPU, memoria, dischi, rete, sensori) in Python. È utile principalmente per il monitoraggio del sistema,
la profilazione e la limitazione delle risorse dei processi e la gestione dei processi in esecuzione.
Implementa molte funzionalità offerte dai classici strumenti a riga di comando UNIX come ps, top, iotop, lsof, netstat, ifconfig, free e altri.  


link: https://github.com/giampaolo/psutil
"""


print(psutil.cpu_times())
print(psutil.cpu_freq(percpu=True))
print(psutil.cpu_count())
print(psutil.cpu_count())