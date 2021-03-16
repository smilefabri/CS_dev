import resource


""" 
funziona solo su sistemi unix

Le funzioni in resource rilevano le risorse del sistema corrente consumate da un processo,
e pongono limiti su di esse per controllare quanto carico un programma può imporre ad un sistema.

link : https://docs.python.org/3.7/library/resource.html

"""

"""
Si usi getrusage() per rilevare le risorse usate dal processo corrente e/o dai suoi figli.
Il valore di ritorno è una struttura dati contenente parecchie metriche di risorse basate sullo stato corrente del sistema.
"""


RESOURCES = [
    ('ru_utime', 'Tempo utente'),
    ('ru_stime', 'Tempo sistema'),
    ('ru_maxrss', 'Dimensione massima memoria\nfisica'
                  ' mappata dal processo     '),
    ('ru_ixrss', 'Dimensione memoria condivisa '),
    ('ru_idrss', 'Dimensione memoria non condivisa'),
    ('ru_isrss', 'Dimensione dello stack'),
    ('ru_inblock', 'Blocchi input'),
    ('ru_oublock', 'Blocchi output'),
]

usage = resource.getrusage(resource.RUSAGE_SELF)

print(usage)
for name, desc in RESOURCES:
    print('{:<32} ({:<10}) = {}'.format(
        desc, name, getattr(usage, name)))


#I limiti possono essere cambiati con setrlimit().