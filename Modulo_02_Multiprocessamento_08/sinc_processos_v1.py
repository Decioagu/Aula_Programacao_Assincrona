from multiprocessing import Process, Value

'''
Este programa ocorre "race conditions", pois as funções de "depositar" e "sacar" ocorre 
de maneira simultânea, sem que haja garantia no ordenamento nas operações das funções.
'''

# 1ª função
def depositar(saldo):
    for _ in range(10_000):
        saldo.value = saldo.value + 1

# 2ª função
def sacar(saldo):
    for _ in range(10_000):
        saldo.value = saldo.value - 1


def realizar_transacoes(saldo):
    pc1 = Process(target=depositar, args=(saldo,))
    pc2 = Process(target=sacar, args=(saldo,))

    pc1.start()
    pc2.start()

    pc1.join()
    pc2.join()


if __name__ == '__main__':
    saldo = Value('i', 100) # 'i' = int

    print(f'Saldo Inicial: {saldo.value}')

    for _ in range(10):
        realizar_transacoes(saldo)
    
    print(f'Saldo Final: {saldo.value}')

