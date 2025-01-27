from time import time
import asyncio

start_time = time()

class BobEsponja:

    start_time = time()
    async def preparar_pao(self):
        print('Preparando pão')
        await asyncio.sleep(3)
        print(f'Pão finalizado: {(time() - self.start_time):.0f} segundos')

    async def preparar_hamburger(self):
        print('Fritar hamburger')
        await asyncio.sleep(10)
        print(f'Hamburger finalizado: {(time() - self.start_time):.0f} segundos')

    async def montar_sanduiche(self):
        print('Montar sanduíche')
        await asyncio.sleep(5)
        print(f'Sanduíche finalizado: {(time() - self.start_time):.0f} segundos')
        print('Montar_sanduiche')

    async def fazer_milkshake(self):
        print('Fazendo milkshake')
        await asyncio.sleep(7)
        print(f'Milkshake finalizado: {(time() - self.start_time):.0f} segundos')

    # Agendamento e agrupamentos de tarefas (1)
    async def pedido(self):
        tarefa11 = self.fazer_sanduiche()
        tarefa12 = self.fazer_milkshake()
        await asyncio.gather(tarefa11, tarefa12)
        print('Mas já...')

    # Agendamento e agrupamentos de tarefas (2)
    async def fazer_sanduiche(self):
        tarefa21 = self.preparar_pao() # corta pão
        tarefa22 = self.preparar_hamburger() # frita
        await asyncio.gather(tarefa21, tarefa22)

        '''
        "asyncio.get_running_loop()"
        Retorna o loop de eventos atualmente em execução na thread onde ela é chamada.
        Quando usar:
        - Dentro de funções assíncronas para obter o loop de eventos que está em execução.
        - Para programar operações diretamente no loop, como adicionar tarefas, agendar 
          callbacks, manipular recursos do loop.

        Diferença para asyncio.get_event_loop():
        - asyncio.get_event_loop() funciona tanto dentro quanto fora de corrotinas 
          e tenta obter o loop de eventos padrão, criando um se necessário.
        - asyncio.get_running_loop() é mais específico e só funciona se um loop 
          de eventos já estiver ativo. É útil para evitar a criação acidental de 
          loops fora do contexto correto.
        '''
        # event_loop = asyncio.get_running_loop() # Retorna o loop
        event_loop = asyncio.get_event_loop() # Retorna o loop
        
        # executar.tarefa(função)
        event_loop.create_task(self.montar_sanduiche()) # Monta
        print(f'Fazer_sanduiche')

cliente = BobEsponja() # Função 

# Loop de eventos assíncrono
asyncio.run(cliente.pedido())

print()
print(f'Tudo pronto, pedido finalizado em {(time() - start_time):.0f} segundos')

# Tudo pronto, pedido finalizado em 10 segundos