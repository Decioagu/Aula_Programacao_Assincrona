import asyncio

# 3 assíncrono
async def soma_03(a, b):
    return a + b

resultado_03 = soma_03(1,3)

# Criando loop de eventos
event_loop_03 = asyncio.new_event_loop()

# Executa o loop de eventos 
final = event_loop_03.run_until_complete(resultado_03)

# Fechando o loop de eventos
event_loop_03.close() # não obrigatório

print(final) # 4

'''
Se você não fechar o loop com ".close()", esses recursos podem não ser 
liberados imediatamente, levando a vazamentos de memória ou outros problemas 
em aplicativos mais complexos.
'''

# -------------------- OU ----------------------

# 4 assíncrono
async def soma_04(a, b):
    return a + b
# execução de função assíncrona (cria, executar, fechar)
print(asyncio.run(soma_04(1,3))) # 4