'''
A diferença principal entre os dois códigos está na forma como as funções são definidas
e executadas, devido ao uso de sincronismo no primeiro caso e assincronismo no segundo.
'''


# A função soma_01 é síncrona, ou seja, o código é executado sequencialmente, linha por linha.
# sincrono
def soma_01(a, b):
    return a + b

resultado_01 = soma_01(1,3)
print(resultado_01) # 4
print()

# ------------------------------------------

# A função soma_02 é declarada com o modificador async, indicando que é uma função assíncrona.
# assíncrono
async def soma_02(a, b):
    return a + b

resultado_02 = soma_02(1,3)
print(resultado_02) # <coroutine object soma_02 at 0x000001F8B1656740>

'''
Objeto <coroutine object soma_02 at 0x000001F8B1656740>, execução paralela em espaço de memória.
Objeto "coroutine" é uma função especial em Python que pode ser pausada e retomada, 
tornando-a uma ferramenta fundamental para programação assíncrona. 
As coroutines são usadas para realizar operações que podem levar tempo 
(como I/O ou aplicação web) sem bloquear a execução de outras partes do programa.
'''

