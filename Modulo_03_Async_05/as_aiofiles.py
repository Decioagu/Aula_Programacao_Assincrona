# import asyncio
# import aiofiles
# import os

# async def exemplo_arq1():
#     # Caminho absoluto baseado no diretório atual do script
#     caminho_arquivo = os.path.join(os.path.dirname(__file__), 'texto.txt')

#     async with aiofiles.open(caminho_arquivo, mode='r') as arquivo:
#         conteudo = await arquivo.read()
#     print(conteudo)


# async def exemplo_arq2():
#     # Caminho absoluto baseado no diretório atual do script
#     caminho_arquivo = os.path.join(os.path.dirname(__file__), 'texto.txt')

#     async with aiofiles.open(caminho_arquivo, mode='r') as arquivo:
#         async for linha in arquivo:
#             print(linha)


# def main():
#     el = asyncio.get_event_loop()

#     el.run_until_complete(exemplo_arq1())
#     print('\n-------------------------------------\n')
#     el.run_until_complete(exemplo_arq2())

#     el.close()


# if __name__ == '__main__':
#     main()

# ======================================== OU =========================================

import asyncio
import aiofiles
import os

async def exemplo_arq1():
    # Caminho absoluto baseado no diretório atual do script
    caminho_arquivo = os.path.join(os.path.dirname(__file__), 'texto.txt')

    async with aiofiles.open(caminho_arquivo, mode='r') as arquivo:
        conteudo = await arquivo.read()
    print(conteudo)


async def exemplo_arq2():
    # Caminho absoluto baseado no diretório atual do script
    caminho_arquivo = os.path.join(os.path.dirname(__file__), 'texto.txt')

    async with aiofiles.open(caminho_arquivo, mode='r') as arquivo:
        async for linha in arquivo:
            print(linha)


async def main():
    await exemplo_arq1()
    print('\n-------------------------------------\n')
    await exemplo_arq2()

if __name__ == '__main__':
    asyncio.run(main())