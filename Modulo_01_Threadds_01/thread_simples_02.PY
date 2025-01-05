from threading import Thread
from time import sleep

# função
def vai_demorar(texto: str, tempo: int): 
    # print('Não vai aguardar') # ative o t1.join() e veja
    sleep(tempo)
    print(texto)

# OBS: args=(tupla)
t1 = Thread(target=vai_demorar, args=('Executando a Thread 1', 5)) # executar em paralelo
t1.start() # iniciar execução
# t1.join() # aguardando execução de toda a thread (executa programa de forma linear)

while t1.is_alive(): #  verificar se uma thread está atualmente em execução
    print('Esperando a Thread 1')
    sleep(2)

print('Finalizado...')