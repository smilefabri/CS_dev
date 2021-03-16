
"""
Il modulo atexit fornisce una interfaccia per registrare funzioni
che saranno chiamate quando un programma si sta normalmente chiudendo.
"""

import atexit

"""
con un decoratore 
@atexit.register
def all_done():
    print('all_done()')

"""

def all_done():
    print('all_done()')

print('In registrazione')
atexit.register(all_done)
print('Registrato')

""" output
In registrazione
Registrato
all_done()
"""

#E' anche possibile registrare più di una funzione, e fornire argomenti alle funzioni registrate


def my_cleanup(name):
    print('my_cleanup({})'.format(name))


atexit.register(my_cleanup, 'primo')
atexit.register(my_cleanup, 'secondo')
atexit.register(my_cleanup, 'terzo')

#Per cancellare un callback di uscita, lo si rimuove dal registro usando unregister().

atexit.unregister(my_cleanup)

"""

I callback registrati con atexit non sono chiamati se si verifica almeno una delle seguenti condizioni:

    Il programma termina a causa di un segnale
    os._exit() viene invocato direttamente
    Viene rilevato un errore fatale nell'interprete

    
"""

