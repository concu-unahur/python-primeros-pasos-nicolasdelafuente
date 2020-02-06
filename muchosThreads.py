import threading
import time
import logging

from tiempo import Contador

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# la función para usar para el thread
def dormir():
    time.sleep(1)


contador = Contador()

contador.iniciar()

lista = [] #creo lista

for i in range(10):
    #crear un thead
    t = threading.Thread(target=dormir, name='thread')
    #logging.info('Thread ')
    #lanzarlo
    t.start()
    lista.append(t) #los cargo en la lista
    #t.join()

for thread in lista:
    thread.join()

contador.finalizar()
contador.imprimir()