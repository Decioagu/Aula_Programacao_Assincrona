from threading import Thread
from time import sleep


def main():
    th = Thread(target=contar, args=('elefante', 10)) # executar em paralelo # (nome, tempo)
    th.start() # iniciar execução da thread

    print('Podemos fazer outras coisas no programa enquanto a thread vai executando...')
    print('Geek University ' * 2)

    th.join()  # aguardando execução da thread

    print('Pronto!')

# função da threads
def contar(nome, tempo):
    for n in range(1, tempo + 1):
        print(f'{n} {nome}(s)...')
        sleep(1)


if __name__ == '__main__':
    main()

