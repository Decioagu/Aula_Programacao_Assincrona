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
        
    async def fazer_milkshake(self):
        print('Fazendo milkshake')
        await asyncio.sleep(7)
        print(f'Milkshake finalizado: {(time() - self.start_time):.0f} segundos')

    # Agendamento e agrupamentos de tarefas 
    async def pedido(self):
        tarefa1 = self.preparar_hamburger()
        tarefa2 = self.preparar_pao()
        tarefa3 = self.fazer_milkshake()
        await asyncio.gather(tarefa1, tarefa2, tarefa3)
        await self.montar_sanduiche()
        

cliente = BobEsponja() # Função 

# Loop de eventos assíncrono
event_loop = asyncio.new_event_loop()
final = event_loop.run_until_complete(cliente.pedido())
event_loop.close()

print()
print(f'Tudo pronto, pedido finalizado em {(time() - start_time):.0f} segundos')

# Tudo pronto, pedido finalizado em 15 segundos