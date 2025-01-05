from multiprocessing import current_process, cpu_count ,Pool

# Função calcular
def calcular(dado):
    return dado ** 2 # [0, 1, 2, 3, 4, 5, 6] ** 2


def imprimir_nome_processo():
    print(f'Iniciando o processo com nome: {current_process().name}') # exibir nome do processo


def main():
    tamanho_pool = cpu_count() * 2 # 8 * 2 = 16 processos

    print(f'Tamanho da Pool: {tamanho_pool}')

    # Pool() distribui "Ns" tarefas para os processos disponíveis de forma eficiente
    pool = Pool(processes=tamanho_pool, initializer=imprimir_nome_processo)
    # Neste caso são criados 16 processos, permitindo até 16 tarefas executados em paralelo

    entradas = list(range(7)) # [0, 1, 2, 3, 4, 5, 6]
    saidas = pool.map(calcular, entradas)

    print(f'Saídas: {saidas}') # [0, 1, 4, 9, 16, 25, 36]

    pool.close() # Fecha o pool para novas tarefas
    pool.join() # Aguarda os processos finalizarem


if __name__ == '__main__':
    main()
