import sqlite3

#serve per creare un  collegamento al tuo database 

conn = sqlite3.connect("nomedatabase.db") #inserire il nome con la sua estensione  

#se vuoi creare un database all'interno della ram al posto del nome metti :memory:

#poi devi creare un'oggetto per muoverti all'interno del tuo database (studianti un po di  sql)
c = conn.cursor()

"""
adesso puoi eseguire 'script sql' all'interno del tuo database con il metodo execute()

"""

c.execute("") #devi inserire il codice sql 


conn.commit() #come sai bene devi sempre fare il commit per confermare le modifiche 

conn.close() #devi sempre chiudere il riferimento al tuo database.