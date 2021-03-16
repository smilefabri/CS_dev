

"""

un decoratore è un una funzione che accetta come parametro un all'altra funzione
lo si usa  per evitare di riscrivere lo stesso codice più volte 
esempio:

"""

#descrivo il mio decoratore
def first_decoratore(f):
    f()
    print("sono il decoratore")



@first_decoratore
def c():
    print("sono la funzione normale")


'''
se non é molto chiaro, proviamo con questo esempio

c = first_decoratore(c)

c() é uguale a quello sopra, ma viene usato quello sopra perché è più efficente 
(poi perchè è più figo)

'''