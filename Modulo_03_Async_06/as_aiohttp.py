# import asyncio
# import aiofiles
# import aiohttp
# import bs4
# import os

# # Ler links no arquivo txt
# async def pegar_links():
#     # Caminho absoluto baseado no diretório atual do script
#     caminho_arquivo = os.path.join(os.path.dirname(__file__), 'links.txt')
    
#     links = []
#     async with aiofiles.open(caminho_arquivo, mode='r') as arquivo:
#         async for link in arquivo:
#             links.append(link.strip())
#     return links

# # Pegar HTML do link (texto)
# async def pegar_html(link):
#     print(f'Pegando o HTML do curso {link}')
#     try:
#         # "aiohttp.ClientSession()" para requisições HTTP
#         async with aiohttp.ClientSession() as session:
#             async with session.get(link, timeout=10) as resp:
#                 resp.raise_for_status()  # Verifica se a resposta foi bem-sucedida (HTTP 200)
#                 return await resp.text() # Retornar texto
#     except aiohttp.ClientError as e:
#         print(f'\nErro ao pegar HTML do link {link}: {e}\n')
#         return None
#     except asyncio.TimeoutError:
#         print(f'\nTempo esgotado para o link {link}\n')
#         return None

# # Extrair título do HTML
# def pegar_titulo(html):
#     soup = bs4.BeautifulSoup(html, 'html.parser')
#     title = soup.select_one('title')
#     return title.text.split('|')[0].strip() if title else 'Título não encontrado'

# # Imprimir títulos dos links
# async def imprimir_titulos():
#     links = await pegar_links()  # Ler links em arquivo txt
#     tarefas = []

#     # Retornar texto de HTML dos links
#     for link in links:
#         tarefas.append(asyncio.create_task(pegar_html(link)))
    
#     # Processar resultados das tarefas
#     for tarefa, link in zip(tarefas, links):
#         html = await tarefa
#         if html:  # Verificar se o HTML foi obtido com sucesso
#             title = pegar_titulo(html)
#         else:
#             title = 'Erro ao obter título'
#         print(f'Curso: {title}')

# # Função principal
# def main():
#     el = asyncio.get_event_loop()
#     el.run_until_complete(imprimir_titulos())
#     el.close()

# # Executar script
# if __name__ == '__main__':
#     main()

# ======================================== OU =========================================

import asyncio
import aiofiles
import aiohttp
import bs4
import os

# Ler links no arquivo txt
async def pegar_links():
    # Caminho absoluto baseado no diretório atual do script
    caminho_arquivo = os.path.join(os.path.dirname(__file__), 'links.txt')
    
    links = []
    async with aiofiles.open(caminho_arquivo, mode='r') as arquivo:
        async for link in arquivo:
            links.append(link.strip())
    return links

# Pegar HTML do link (texto)
async def pegar_html(link):
    print(f'Pegando o HTML do curso {link}')
    try:
        # "aiohttp.ClientSession()" para requisições HTTP
        async with aiohttp.ClientSession() as session:
            async with session.get(link, timeout=10) as resp:
                resp.raise_for_status()  # Verifica se a resposta foi bem-sucedida (HTTP 200)
                return await resp.text() # Retornar texto
    except aiohttp.ClientError as e:
        print(f'\nErro ao pegar HTML do link {link}: {e}\n')
        return None
    except asyncio.TimeoutError:
        print(f'\nTempo esgotado para o link {link}\n')
        return None

# Extrair título do HTML
def pegar_titulo(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    title = soup.select_one('title')
    return title.text.split('|')[0].strip() if title else 'Título não encontrado'

# Imprimir títulos dos links
async def imprimir_titulos():
    links = await pegar_links()  # Ler links em arquivo txt
    tarefas = []

    # Retornar texto de HTML dos links
    for link in links:
        tarefas.append(asyncio.create_task(pegar_html(link)))
    
    # Processar resultados das tarefas
    for tarefa, link in zip(tarefas, links):
        html = await tarefa
        if html:  # Verificar se o HTML foi obtido com sucesso
            title = pegar_titulo(html)
        else:
            title = 'Erro ao obter título'
        print(f'Curso: {title}')

# Função principal
async def main():
    await imprimir_titulos()

# Executar script
if __name__ == '__main__':
    asyncio.run(main())