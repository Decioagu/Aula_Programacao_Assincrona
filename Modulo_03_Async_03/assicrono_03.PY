import asyncio

# assíncrono
async def soma_07(a, b):
    print('Iniciar soma_07')
    await asyncio.sleep(1)
    print('finalizado soma_07')
    return a + b

async def subtr_07(a, b):
    print('Iniciar subt_07')
    await asyncio.sleep(6)
    print('finalizado subt_07')
    return a - b

async def mult_07(a, b):
    print('Iniciar mult_07')
    await asyncio.sleep(1)
    print('finalizado mult_07')
    return a * b

async def div_07(a, b):
    print('Iniciar div_07')
    await asyncio.sleep(3)
    print('finalizado div_07')
    return a / b

print()
# "Criando" loop de eventos
event_loop_07 = asyncio.new_event_loop()
print()

# "Agendar" a execução
tarefa1 = event_loop_07.create_task(soma_07(1,2))
tarefa2 = event_loop_07.create_task(subtr_07(1,2))
tarefa3 = event_loop_07.create_task(mult_07(1,2))
tarefa4 = event_loop_07.create_task(div_07(1,2))


#  "Agrupar" tarefas Agendadas
tarefas = asyncio.gather(tarefa1, tarefa2, tarefa3, tarefa4)
print('Aguardando...') ### 1

# "Executa" o loop de eventos (forme ordenada)
resultados = event_loop_07.run_until_complete(tarefas) ### 2

# Exibir resultados
print()
print("Resultados das funções:", resultados)
print()

# .result() retorna o valor de cada função específica após a execução
print("Retorno da soma:", tarefa1.result())
print("Retorno da subtração:", tarefa2.result())
print("Retorno da multiplicação:", tarefa3.result())
print("Retorno da divisão:", tarefa4.result())

# Fechando o loop de eventos
event_loop_07.close() # não obrigatório
print()
print('Décio Santana de Aguiar') ### 3

# -------------------- OU ----------------------

print()

import asyncio

# assíncrono
async def soma_08(a, b):
    print('Iniciar soma_08')
    await asyncio.sleep(1)
    print('finalizado soma_08')
    return a + b

async def subtr_08(a, b):
    print('Iniciar subt_08')
    await asyncio.sleep(6)
    print('finalizado subt_08')
    return a - b

async def mult_08(a, b):
    print('Iniciar mult_08')
    await asyncio.sleep(1)
    print('finalizado mult_08')
    return a * b

async def div_08(a, b):
    print('Iniciar div_08')
    await asyncio.sleep(3)
    print('finalizado div_08')
    return a / b

async def main():
    # Armazenar funções em variáveis
    func_1 = soma_08(1, 2)
    func_2 = subtr_08(1, 2)
    func_3 = mult_08(1, 2)
    func_4 = div_08(1, 2)

    print('Aguardando...') ### 1
    
    #  Execução de grupo de funções
    resultados = await asyncio.gather(func_1, func_2, func_3, func_4) ### 2

    # Exibir resultados
    print()
    print("Resultados das funções:", resultados)
    print()

    # Exibir os resultados específicos
    print("Retorno da soma:", resultados[0])
    print("Retorno da subtração:", resultados[1])
    print("Retorno da multiplicação:", resultados[2])
    print("Retorno da divisão:", resultados[3])

# Executar o programa principal (Cria, Executar, Fechar)
asyncio.run(main())
print()
print('Décio Santana de Aguiar') ### 3


