from multiprocessing import Process
from time import sleep

'''
Calcular valores nas funções 1 e 2 conforme status (Verdadeiro ou Falso)
"status" é uma variável compartilhada entre as duas funções porem valor de "status", 
não altear dentro das funções, ou seja, alteração de "status" dentro da funcao1 não é
compartilhada na funcao2, a reciproca é verdadeira. 
'''

def funcao1(val, stat):
    if stat: # stat = True (300)
        print(stat, end=' | ')
        res = val + 200
        stat = False # alteração de "status" irrelevante na "funçao2"
    else: # stat = False (500)
        print(stat, end=' | ')
        res = val + 400
        val = 50 # irrelevante fora da "funçao1"
        stat = True # alteração de "status" irrelevante na "funçao2"
    
    print(f'O resultado da função 1 é {res}')
    sleep(0.001)


def funcao2(val, stat):
    if stat: # stat = True (200)
        print(stat, end=' | ')
        res = val + 100
        stat = False # alteração de "status" irrelevante na "funçao1"
    else: # stat = False (400)
        print(stat, end=' | ')
        res = val + 300
        val = 50 # irrelevante fora da "funçao2"
        stat = True # alteração de "status" irrelevante na "funçao1"
    
    print(f'O resultado da função 2 é {res}')
    sleep(0.001)


def main():
    valor = 100
    status = True # (False ou True) | valor alterado NÃO compartilhado entre funções

    p1 = Process(target=funcao1, args=(valor, status))  # executar em paralelo
    p2 = Process(target=funcao2, args=(valor, status))  # executar em paralelo

    # ordem p1 e p2
    p1.start() # True (O resultado da função 1 é 300) | False (O resultado da função 1 é 500)
    p2.start() # True (O resultado da função 2 é 200) | False (O resultado da função 2 é 400)

    # ordem p2 e p1
    # p2.start() # True (O resultado da função 2 é 200) | False (O resultado da função 2 é 400)
    # p1.start() # True (O resultado da função 1 é 300) | False (O resultado da função 1 é 500)   

    p1.join() # Aguarda o término do processo
    p2.join() # Aguarda o término do processo


if __name__ == '__main__':
    main()
