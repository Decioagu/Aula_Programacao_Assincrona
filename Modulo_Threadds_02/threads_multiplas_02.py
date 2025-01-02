
from threading import Thread
from time import sleep


class MeuThread(Thread): # executar em paralelo
    def __init__(self, texto: str, tempo: int):
        self.texto = texto
        self.tempo = tempo
        # executar threading.Thread (obrigatório)
        super().__init__() # ou Thread.__init__(self)
        
    def run(self): # método que será executado
        sleep(self.tempo) # espera
        print(self.texto)


t1 = MeuThread('Thread 1', 9) # (nome, tempo)
t1.start() # executa a classe em paraleto
# t1.join() # aguardando execução de toda a thread (executa programa de forma linear)

t2 = MeuThread('Thread 2', 6) # (nome, tempo)
t2.start() # executa a classe em paraleto
# t1.join() # aguardando execução de toda a thread (executa programa de forma linear)

t3 = MeuThread('Thread 3', 3) # (nome, tempo)
t3.start() # executa a classe em paraleto
t1.join() # aguardando execução de toda a thread (executa programa de forma linear)

for i in range(12):
    print(i)
    sleep(1) # espera