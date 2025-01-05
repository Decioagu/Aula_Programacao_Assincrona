from threading import Thread
import random
from time import sleep

from typing import List

'''
Este programa ocorre "race conditions", pois a operação de transferência entre contas bancárias
ocorre de maneira simultânea, sem que haja garantia de ordenamento nos valores das operações
de transferência.
'''

# Classe geradora de contas bancárias com saldo
class Conta: # 2.1
    def __init__(self, saldo=0) -> None:
        self.saldo = saldo

def main():
    contas = criar_contas() # 2 (Lista com 6 contas bancárias)

    total = sum(conta.saldo for conta in contas) # 3 (Soma os valores de todas as 6 contas)
    print('Iniciando transferências...')

    # Múltiplas Threads de operação servicos => transferência ("race conditions")
    tarefas = [ # 4
        Thread(target=servicos, args=(contas, total)), # 4
        Thread(target=servicos, args=(contas, total)), # 4.1
        Thread(target=servicos, args=(contas, total)), # 4.1
        Thread(target=servicos, args=(contas, total)), # 4.1
        Thread(target=servicos, args=(contas, total)), # 4.1
        Thread(target=servicos, args=(contas, total))  # 4.1
    ]

    [tarefa.start() for tarefa in tarefas] # 5
    [tarefa.join() for tarefa in tarefas]  # 6

    print('Transferências completas.')
    valida_banco(contas, total) # 7

# Transferir valores entre duas contas na (Lista com 6 contas bancárias)
def servicos(contas, total): # 4.1
    for _ in range(1, 1_000): # -> 999 repetições <-
        c1, c2 = pega_duas_contas(contas) # 4.1.1
        valor = random.randint(1, 100) # sorteia valores entre 1 e 100
        transferir(c1, c2, valor) # 4.1.2
        valida_banco(contas, total) # 4.1.3

# Gera uma Lisa com 6 contas bancárias e saldo
def criar_contas() -> List[Conta]: # 2
    # Cada conta tem valores sortidos entre 5000 e 10000
    return [
        Conta(saldo=random.randint(5_000, 10_000)), # 2.1
        Conta(saldo=random.randint(5_000, 10_000)), # 2.1
        Conta(saldo=random.randint(5_000, 10_000)), # 2.1
        Conta(saldo=random.randint(5_000, 10_000)), # 2.1
        Conta(saldo=random.randint(5_000, 10_000)), # 2.1
        Conta(saldo=random.randint(5_000, 10_000)), # 2.1
    ]

# Seleciona aleatoriamente duas contas entre (Lista com 6 contas bancárias)
def pega_duas_contas(contas): # 4.1.1
    c1 = random.choice(contas) # selecionar aleatoriamente um elemento de uma sequência
    c2 = random.choice(contas) # selecionar aleatoriamente um elemento de uma sequência

    while c1 == c2: # selecione outra conta c2 caso seja igual a c1
        c2 = random.choice(contas)
    
    return c1, c2

# Transfere valores ente duas contas desde que haja saldo suficiente (conta destino, conta origem)
def transferir(origem: Conta, destino: Conta, valor: int): # 4.1.2
    if origem.saldo < valor: # finaliza caso conta de origem saldo insuficiente
        return
    origem.saldo -= valor
    sleep(0.001)
    destino.saldo += valor

# Imprimir valores das contas bancárias apos operações de transferência
def valida_banco(contas: List[Conta], total: int): # 4.1.3
    atual = sum(conta.saldo for conta in contas)

    # confere se apos operação de transferência a diferença entre antes(total) e depois(atual) 
    if atual != total:
        print(f'ERRO: Balanço bancário inconsistente. BRL$ {atual:.2f} vs {total:.2f}', flush=True)
    else:
        print(f'Tudo certo: Balanço bancário consistente: BRL$ {total:.2f}', flush=True)

if __name__ == '__main__':
    main() # 1

