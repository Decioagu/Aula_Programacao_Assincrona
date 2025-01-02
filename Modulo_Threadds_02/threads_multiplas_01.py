from threading import Thread
from time import sleep

def main():
    threads = [
       Thread(target=contar, args=('elefante', 3)),
       Thread(target=contar, args=('buraco', 9)),
       Thread(target=contar, args=('moeada', 12)),
       Thread(target=contar, args=('pato', 3))
    ] 

    [th.start() for th in threads] # executar em paralelo

    print('Podemos fazer outras coisas no programa enquanto a thread vai executando...')
    print('Geek University ' * 2)

    [th.join() for th in threads]  # aguardando execução de toda a thread (executa programa de forma linear)

    for t in threads:
        while t.is_alive(): #  verificar se uma thread está atualmente em execução
            print('\nEsperando as Threads')
            sleep(1)

    print('Pronto, acabou!!!')

# função da threads
def contar(o_que, numero):
    for n in range(1, numero + 1):
        print(f'{n} {o_que}(s)...')
        sleep(1)

if __name__ == '__main__':
    main()

