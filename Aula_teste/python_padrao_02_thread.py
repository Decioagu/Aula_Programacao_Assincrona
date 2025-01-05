from datetime import datetime
import math

from threading import Thread
import multiprocessing

'''
O módulo multiprocessing no Python permite a criação e o gerenciamento de processos
paralelos, aproveitando múltiplos núcleos de CPU para executar tarefas simultaneamente.

Diferença entre "threading" e "multiprocessing":
- "threading": Usa threads, que compartilham o mesmo espaço de memória, mas são limitadas pelo
Global Interpreter Lock (GIL), o que pode reduzir o desempenho em operações intensivas de CPU.

- "multiprocessing": Usa processos, cada um com seu próprio espaço de memória, eliminando o GIL 
e permitindo melhor aproveitamento de CPUs multicore.
'''


### Tempo de processamento ###

def main():
    qtd_cores = multiprocessing.cpu_count() # contagem de número de núcleos do processador
    print(f'Realizando o processamento matemático com {qtd_cores} core(s).')

    inicio = datetime.now() # tempo inicial

    threads = [] # Lista de Thread

    # dividi processamento da (Função) por número de núcleo do processador
    for n in range(1, qtd_cores + 1):
        ini = 50_000_000 * (n - 1) / qtd_cores 
        fim = 50_000_000 * n / qtd_cores
        print(f'Core {n} processando de {ini} até {fim}')
        threads.append(
            Thread(
                target=computar,
                kwargs={'inicio': ini, 'fim': fim},
                daemon=True
            )
        )
    '''
    "daemon=True" é execução de processo em segundo plano e não impedem que o programa principal termine,
    é útil para tarefas que podem ou devem ser interrompidas quando o programa principal termina.
    '''
    
    [th.start() for th in threads] # iniciar Threads
    [th.join() for th in threads] # Aguardar finalização de Threads

    tempo = datetime.now() - inicio # tempo final

    print(f"Terminou em {tempo.total_seconds():.2f} segundos.") # informa tempo utilizado pela (Função)


# (Função) processo de calculo matemático
def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == '__main__':
    main()


"""
Terminou em 14.82 segundos.
"""
