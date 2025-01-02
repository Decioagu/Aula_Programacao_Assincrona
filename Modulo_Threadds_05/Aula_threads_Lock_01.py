# Threads - Executando processamentos em paralelo

from threading import Lock, Thread
from time import sleep

class Ingressos:
    """
    Classe que vende ingressos
    """

    def __init__(self, estoque: int):
        """ Inicializando...
        :param estoque: quantidade de ingressos em estoque
        """
        self.estoque = estoque # quantidade em estoque
        self.lock = Lock() ### Bloqueio

    def comprar(self, quantidade: int):
        """
        Compra determinada quantidade de ingressos
        :param quantidade: A quantidade de ingressos que deseja comprar
        :type quantidade: int
        :return: Nada
        :rtype: None
        """
        
        self.lock.acquire() ### Tranca o método

        if self.estoque < quantidade:
            if quantidade == 1:
                print(f'Quero {quantidade} ingresso.')
            else:
                print(f'Quero {quantidade} ingressos.')
            print('Não temos ingressos suficientes.')
            print()
            self.lock.release() ### Libera o método
            return

        sleep(1) # atraso proposital (retirar sincronia da class)

        self.estoque -= quantidade
        if quantidade == 1:
            print(f'Quero {quantidade} ingresso.')
        else:
            print(f'Quero {quantidade} ingressos.')
        print(f'Você comprou {quantidade} ingresso(s).')
        if self.estoque != 0:
            print(f'Ainda temos {self.estoque} em estoque.')
            print()
        else:
            print(f'Ingressos esgotados.')
        
        self.lock.release() ### Libera o método


if __name__ == '__main__':
    ingressos = Ingressos(11) # quantidade em estoque

    for i in range(1, 10):
        t = Thread(target=ingressos.comprar, args=(i,)) # executar em paralelo 
        t.start() # iniciar execução

    t = Thread(target=ingressos.comprar, args=(1,)) # executar em paralelo 
    t.start()

    print('Total de ingresso=',ingressos.estoque) # ver quantidade de ingresso inicial