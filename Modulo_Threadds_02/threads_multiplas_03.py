
from threading import Thread
from time import sleep

# função
def vai_demorar(texto: str, tempo: int): 
    sleep(tempo)
    print(texto)

# OBS: args=(tupla)
t1 = Thread(target=vai_demorar, args=('Thread 1', 5)) # executar em paralelo
t1.start() # iniciar execução
t1.join() # aguardando execução de toda a thread (executa programa de forma linear)

t2 = Thread(target=vai_demorar, args=('Thread 2', 1)) # executar em paralelo
t2.start() # iniciar execução
# t2.join() # aguardando execução de toda a thread (executa programa de forma linear)

t3 = Thread(target=vai_demorar, args=('Thread 3', 3)) # executar em paralelo
t3.start() # iniciar execução
# t3.join() # aguardando execução de toda a thread (executa programa de forma linear)

for i in range(12):
    print(i)
    sleep(.5)