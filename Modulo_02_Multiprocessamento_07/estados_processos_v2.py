from multiprocessing import Process, Value
from time import sleep
import ctypes

'''
# Sem compartilhamento de dados.
Calcular valores nas funções 1 e 2 conforme status (Verdadeiro ou Falso)
"módulo ctypes" permite que a variável "status" compartilhada alterações de valor entre as 
funções 1 e 2, ou seja, alteração de "status" dentro da funcao1 é compartilhada na funcao2,
a reciproca é verdadeira.
'''

def funcao1(val, stat):
    if stat.value: # stat = True
        print(stat, end=' | ')
        res = val.value + 200
        stat.value = False # alteração de "status"
    else: # stat = False
        print(stat, end=' | ')
        res = val.value + 400
        val.value = 50 # valor de "status" alterado
        stat.value = True # alteração de "status"
    
    print(f'O resultado da função 1 é {res}')
    sleep(0.001)


def funcao2(val, stat):
    if stat.value: # stat = True
        print(stat, end=' | ')
        res = val.value + 100
        stat.value = False # alteração de "status"
    else: # stat = False 
        print(stat, end=' | ')
        res = val.value + 300
        val.value = 50 # valor de "status" alterado
        stat.value = True # alteração de "status"
    
    print(f'O resultado da função 2 é {res}')
    sleep(0.001)


def main():
    valor = Value('i', 100)
    status = Value(ctypes.c_bool, False) # (False ou True) | valor alterado COMPARTILHADO entre funções

    p1 = Process(target=funcao1, args=(valor, status)) # executar em paralelo
    p2 = Process(target=funcao2, args=(valor, status)) # executar em paralelo

    # ordem p1 e p2
    # p1.start() # True (O resultado da função 1 é 300) | False (O resultado da função 1 é 500)
    # p2.start() # True (O resultado da função 2 é 700) | False (O resultado da função 2 é 150)

    # ordem p2 e p1
    p2.start() # True (O resultado da função 2 é 200) | False (O resultado da função 2 é 400)
    p1.start() # True (O resultado da função 1 é 250) | False (O resultado da função 1 é 500)

    p1.join() # Aguarda o término do processo
    p2.join() # Aguarda o término do processo


if __name__ == '__main__':
    main()
