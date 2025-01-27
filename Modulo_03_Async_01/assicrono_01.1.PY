import asyncio

# 3 assíncrono
async def soma_03(a, b):
    return a + b

funcao = soma_03(1,3)

# Criando loop de eventos | (Cria)
event_loop_03 = asyncio.new_event_loop()
# Executa o loop de eventos | (Executar)
resultado_03 = event_loop_03.run_until_complete(funcao)
# Fechando o loop de eventos | (Fechar)
event_loop_03.close() # não obrigatório

print(resultado_03) # 4

'''
Se você não fechar o loop com ".close()", esses recursos podem não ser 
liberados imediatamente, levando a vazamentos de memória ou outros problemas 
em aplicativos mais complexos.
'''

# -------------------- OU ----------------------

# 4 assíncrono
async def soma_04(a, b):
    return a + b

# Execução da função assíncrona | (Cria, Executar, Fechar)
resultado_04 = asyncio.run(soma_04(1,3))

print(resultado_04) # 4