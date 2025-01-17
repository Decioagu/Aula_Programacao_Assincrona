from multiprocessing import Process, Value, RLock

'''
O uso de Lock() ou RLock() garante que apenas um "multiprocessing" execute um bloco 
específico de código por vez, eliminando o problema de "race conditions" em 
compartilhamento do mesmo recursos ou objeto por múltiplos processos.
'''
# 1ª função
def depositar(saldo, lock): ### (TRAVA)
    for _ in range(10_000):
        with lock: ### (TRAVA)
            saldo.value = saldo.value + 1

# 2ª função
def sacar(saldo, lock): ### (TRAVA)
    for _ in range(10_000):
        with lock: ### (TRAVA)
            saldo.value = saldo.value - 1


def realizar_transacoes(saldo, lock): ### (TRAVA)
    pc1 = Process(target=depositar, args=(saldo, lock)) ### (TRAVA)
    pc2 = Process(target=sacar, args=(saldo, lock)) ### (TRAVA)

    pc1.start()
    pc2.start()

    pc1.join()
    pc2.join()


if __name__ == '__main__':
    saldo = Value('i', 100) # 'i' = int

    lock = RLock() ### Garante execução de bloco (TRAVA)

    print(f'Saldo Inicial: {saldo.value}')

    for _ in range(10):
        realizar_transacoes(saldo, lock) ### (TRAVA)
    
    print(f'Saldo Final: {saldo.value}')

