import asyncio

# assíncrono
async def soma_05(a, b):
    return a + b

async def print_soma(a, b):
    resultado_05 = await soma_05(a, b) # aguarda execução até conclusão. 
    print(resultado_05)

print()
# Criando loop de eventos
event_loop_05 = asyncio.new_event_loop()
# Executa o loop de eventos 
final = event_loop_05.run_until_complete(print_soma(1,3))
# Fechando o loop de eventos
event_loop_05.close() # não obrigatório

# -------------------- OU ----------------------

# assíncrono
async def soma_06(a, b):
    return a + b

async def print_soma(a, b):
    resultado_06 = await soma_06(a, b) # aguarda execução até conclusão.
    print(resultado_06)

print()
# execução de função assíncrona (cria, executar, fechar)
asyncio.run(print_soma(1,3))