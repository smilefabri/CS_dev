""" 
Il modulo io fornisce accesso alla funzione built-in open()
ed alle classi utilizzate per implementare operazioni di input ed output basate su file.
Le classi sono decomposte in modo tale che possano essere ricombinate per scopi alternativi,
ad esempio per abilitare la scrittura di dati in formato Unicode verso un socket di rete.

"""

# io_stringio.py
import io
# Scrittura verso un buffer
"""
La classe StringIO fornisce anche un metodo seek() per muoversi all'interno del buffer quando si è in lettura
"""
output = io.StringIO()
output.write('Questo va nel buffer. ')
print('Anche questo.', file=output)
# Recupero dei valori scritti
print(output.getvalue())
output.close()  # scarica il buffer in memoria
# Inizializza un buffer in lettura
input = io.StringIO('Valore iniziale per il buffer in lettura')
# Legge dal buffer
print(input.read())

"""
Flussi di byte grezzi come i socket possono essere impacchettati in uno strato per gestire la codifica e la decodifica,
facilitandone l'uso con dati di testo. La classe TextIOWrapper supporta sia la lettura che la scrittura.
L'argomento write_through disabilita il buffering,
e scarica tutti i dati scritti all'impacchettatore verso il buffer sottostante immediatamente.
"""

# Scrittura verso un buffer
output = io.BytesIO()
wrapper = io.TextIOWrapper(
    output,
    encoding='utf-8',
    write_through=True,
)
wrapper.write('Questo va nel buffer. ')
wrapper.write('ÁÇÊ')

# Recupero dei valori scritti
print(output.getvalue())

output.close()  # scarica il buffer in memoria

# Inizializza un buffer in lettura
input = io.BytesIO(
    b'Valore iniziale per il buffer in lettura' + 'ÁÇÊ'.encode('utf-8')
)
wrapper = io.TextIOWrapper(input, encoding='utf-8')

# Legge dal buffer
print(wrapper.read())

