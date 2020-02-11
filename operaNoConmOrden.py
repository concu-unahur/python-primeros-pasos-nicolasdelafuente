import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


#definí dos funciones: sumarUno y multiplicarPorDos, que operen sobre la misma variable;
#dale un valor inicial a la variable;

#suma siempre 4 sin importar el orden del thread

cant = 1
lock = threading.Lock() #Hago que los threads se sincronicen (se esperan entre si)

lock.acquire()

def sumarUno():
    global cant
    #global lock
    try: 
        #lock.acquire() #hasta q no dejo la vairiable, nadie puede hacer nada
        cant += 1
    finally:   
        lock.release()

def multiplicarPorDos():
    global cant
    global lock
    try: 
        lock.acquire()
        cant *= 2
    finally:   
        lock.release()
    

#ejecutá cada función en un thread separado y anotá los resultados.

t1 = threading.Thread(target=sumarUno, name='t1')
t2 = threading.Thread(target=multiplicarPorDos, name='t2')

t2.start()
t1.start()


t2.join()

logging.info(t1)
logging.info(t2)

print(f'Cantidad vale {cant}')