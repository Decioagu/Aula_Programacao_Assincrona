from time import sleep
import colorama

from threading import Thread
from queue import Queue

def gerador_de_dados(queue):
    for i in range(1, 11):
        print(colorama.Fore.GREEN + f'Dados {i} gerado.', flush=True) #  flush=True, exibe o texto em tempo real.
        sleep(2)
        queue.put(i) # put(item): Insere um item na fila.


def consumidor_de_dados(queue):
    while queue.qsize() > 0: # qsize(): indica a quantidade de itens atualmente na fila.
        valor = queue.get() # get(): Remove e retorna o primeiro item da fila.
        print(colorama.Fore.RED + f'Dado {valor * 2} processado.', flush=True) #  flush=True, exibe o texto em tempo real.
        sleep(1)
        queue.task_done() # task_done(): Indica que uma tarefa obtida com get() foi concluída.


if __name__ == '__main__':
    print(colorama.Fore.WHITE + 'Sistema iniciado', flush=True) #  flush=True, exibe o texto em tempo real.
    queue = Queue() # estrutura de fila de objetos
    th1 = Thread(target=gerador_de_dados, args=(queue,)) # executar em paralelo
    th2 = Thread(target=consumidor_de_dados, args=(queue,)) # executar em paralelo

    th1.start() # iniciar execução da thread
    th1.join() # aguardando execução da thread

    th2.start() # iniciar execução da thread
    th2.join() # aguardando execução da thread

    '''
    Thread "th1" e "th2" compartilham da mesma fila "queue = Queue()", mesmo dado ou objeto, 
    é necessário garantir que "th1" execute antes de "th2" ou "th2" não ira executar.
    th1.join(): garante que "th1" será executado por completo antes da execução do "th2".
    '''

