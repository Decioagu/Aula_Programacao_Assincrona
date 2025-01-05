from multiprocessing import Queue, Process

def ping(queue):
    msg = 'Décio'
    queue.put(msg) # Insere um item na fila
    print(msg)

def pong(queue):
    msg = queue.get() # Remove e retorna o primeiro item da fila
    print(f'{msg} Santana')
    queue.put(f'{msg} Santana')

def pung(queue):
    msg = queue.get() # Remove e retorna o primeiro item da fila
    print(f'{msg} de Aguiar') # Insere um item na fila

def main():
    queue = Queue() # estruturas de fila

    p1 = Process(target=ping, args=(queue,)) # executar em paralelo
    p2 = Process(target=pong, args=(queue,)) # executar em paralelo
    p3 = Process(target=pung, args=(queue,)) # executar em paralelo


    p1.start() # Inicia o processo
    p2.start() # Inicia o processo
    p3.start() # Inicia o processo

    p1.join() # Aguarda o término do processo
    p2.join() # Aguarda o término do processo
    p3.join() # Aguarda o término do processo


if __name__ == '__main__':
    main()
