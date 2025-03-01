import datetime
import math
import asyncio

def main():
    print('Realizando o processamento matemático de forma assíncrona.')

    el = asyncio.get_event_loop()

    inicio = datetime.datetime.now()

    # el.run_until_complete(computar(inicio=1, fim=50_000_000))
    tarefa1 = el.create_task(computar(inicio=1, fim=10_000_000))
    tarefa2 = el.create_task(computar(inicio=10_000_001, fim=20_000_000))
    tarefa3 = el.create_task(computar(inicio=20_000_0001, fim=30_000_000))
    tarefa4 = el.create_task(computar(inicio=30_000_0001, fim=40_000_000))
    tarefa5 = el.create_task(computar(inicio=40_000_0001, fim=50_000_000))

    tarefas = asyncio.gather(tarefa1, tarefa2, tarefa3, tarefa4, tarefa5)
    el.run_until_complete(tarefas)
    
    tempo = datetime.datetime.now() - inicio

    print(f'Terminou em {tempo.total_seconds():.2f} segundos.')

async def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))

if __name__ == '__main__':
    main()

"""
Forma 1: Terminou em 13.29 segundos.
Forma 2: Terminou em 4.87 segundos.
Forma 3: Terminou em .87 segundos.
"""
