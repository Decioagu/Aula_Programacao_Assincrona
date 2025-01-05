from multiprocessing import current_process, Process

def faz_algo(valor):
    print(f'3º Fazendo algo com o {valor}') # 3


def main():
    print(f'1º Iniciando o processo com nome: {current_process().name}') # 1
    '''
    "current_process()"
    Permite acessar informações sobre o processo em execução, 
    como o nome, ID (PID), status e se ele é o processo principal.
    '''
    pc = Process(target=faz_algo, args=('Pássaro',), name='Processo Geek') # executar em paralelo
    print(f'2º Iniciando o processo com nome: {pc.name}') # 2

    pc.start() # Inicia o processo
    pc.join() # Aguarda o término do processo


if __name__ == '__main__':
    main()
