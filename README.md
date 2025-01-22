# Aula_Programacao_Assincrona
 Programação Concorrente e Assíncrona com Python

## Threads
- Em Python, __threads__ são linhas de execução concorrentes em um mesmo processo. Elas são concorrentes no sentido de que executam simultaneamente. Isso pode ser útil para melhorar o desempenho de um programa, pois __permite que ele execute múltiplas tarefas ao mesmo tempo__.
---

**Aula_teste**
- Realização de teste utilizando diversos processos no mesmo programa:
    - python_padrao_01.py
    - python_padrao_02_thread.py
    - python_padrao_03_multiprocessos.py

**Modulo_Threadds_01**
- Threads simples
    - __Thread(target=???, args=(???))__
        - __Thread()__:  classe do módulo threading que permite criar e gerenciar threads
        - __target()__: define a função que será executada pela thread
        - __args()__: argumentos passados em forma de tupla para função
    - __.start()__: iniciar execução da thread
    - __.join()__: aguardando execução da thread

**Modulo_Threadds_02**
- Múltiplas Threads sem conflito, compartilhamento de dados (mesmo objeto).
---

**Modulo_Threadds_03**
- __compartilhamento_com_threads.py__:
    - Neste exemplo existe conflito entre duas threads "th1" e "th2", onde duas tarefas independentes compartilham o mesmo objeto causando conflitos e falha na execução das tarefas __("race conditions")__, onde caso "th1" não execute por completo "th2" não executará por falta de informação.

    - O __módulo Colorama__ em Python é amplamente utilizado para formatar o texto exibido no terminal com cores, estilos e outras personalizações.
    - O __Queue__ é uma classe do módulo __queue__ em Python, usada para implementar estruturas de fila. Filas são coleções ordenadas o primeiro elemento inserido é o primeiro a ser removido. Essa classe é requentemente utilizada em cenários de __multithreading__ para gerenciar dados compartilhados entre __threads__ de forma segura e eficiente.
---

**Modulo_Threadds_04 & Modulo_Threadds_05**
- __Compartilhamento de dados em múltiplas Threads.__
    - __banco_inseguro.py__:
        - Neste exemplo __existe conflito entre múltiplas Threads__ onde as operações de serviços ocorre de maneira simultânea, ocasionando erro de valores __("race conditions")__, pois as Threads compartilham o mesmo recurso (objeto).

    - __banco_seguro.py__:
        - Neste exemplo foi __eliminado o conflito de múltiplas Threads__ com o uso de __RLock()__, função garantidora que apenas uma Thread por vez execute um bloco específico de código, preservando a consistência do recurso (objeto).

    - __Lock()__ ou __RLock()__ em Python garante que apenas uma Thread por vez execute um bloco específico de código.
        
        Quando usar cada um?
        Use __Lock__:
        Quando o lock será adquirido e liberado apenas uma vez por Thread em cada ciclo.
        Exemplo: __Aula_threads_Lock_01.py & Aula_threads_Lock_02.py__
        
        Use __RLock__:
        Quando uma thread precisa adquirir o lock várias vezes.
        Exemplo: __banco_seguro.py__
---

## Multiprocessamento
- O __módulo multiprocessing__ no Python permite a criação e o gerenciamento de __processos paralelos__, aproveitando múltiplos núcleos de CPU para executar tarefas simultaneamente.

- Diferença entre __"threading"__ e __"multiprocessing"__:
    - __"threading"__: Usa threads, que compartilham o mesmo espaço de memória, mas são limitadas pelo Global Interpreter Lock (GIL), o que pode reduzir o desempenho em operações intensivas de CPU.

    - __"multiprocessing"__: Usa processos, cada um com seu próprio espaço de memória, eliminando o GIL e permitindo melhor aproveitamento de CPUs multicore.
---

**Modulo_02_Multiprocessamento_01**
- A diferença entre __Multiprocessing__ e __Threads__ em Python está relacionada à forma como eles utilizam recursos do sistema e ao tipo de paralelismo que proporcionam.

__Threads__: Threads são unidades de execução mais leves que fazem parte de um único processo. Elas compartilham o mesmo espaço de memória do processo principal.

__Multiprocessing__: Cada processo no multiprocessing tem sua própria instância do interpretador Python e não compartilha memória com outros processos.
---

**Modulo_02_Multiprocessamento_02**
- Alternância de __Multiprocessing__ e __Threads__ em uma única linha.
---

**Modulo_02_Multiprocessamento_03**

- __multiprocessing.current_process().name__: é usada para obter o nome do processo atual em execução.
- __Process(target=???, args=(???,), name='???')__:
    - __Thread()__:  classe do módulo __multiprocessing__ que permite criar e gerenciar execução paralela de código
    - __target()__: define a função que será executada pela thread
    - __args()__: argumentos passados em forma de tupla para função
    - __name()__: define um nome para o processo
- __.start()__: # Inicia o processo
- __.join()__: # Aguarda o término do processo
---

**Modulo_02_Multiprocessamento_04**
- __pool = multiprocessing.Pool()__: gerenciar tarefas para os processos disponíveis de forma eficiente permite executar tarefas em paralelo utilizando múltiplos processos, aproveitando os vários núcleos disponíveis no processador. Possibilitado ao programador manipular a quantidade de processos a ser executado. 
- __pool.close()__: Fecha o pool para novas tarefas
- __pool.join()__: Aguarda os processos finalizarem
---

**Modulo_02_Multiprocessamento_05**
- __Compartilhamento de dados em múltiplas processos__
    - O __método multiprocessing.Pipe()__ cria um canal de comunicação (pipe) __entre dois processos__ que pode ser usado para trocar dados. Esse método retorna um par de conexões (duas extremidades do pipe) que permitem que os processos se comuniquem entre si.
---

**Modulo_02_Multiprocessamento_06**
- __Compartilhamento de dados em múltiplas processos__
    - O __Queue é uma classe do módulo queue__ em Python, usada para implementar estruturas de fila. Filas são coleções ordenadas, onde o primeiro elemento inserido é o primeiro a ser removido. Essa classe é frequentemente utilizada em cenários de multithreading para gerenciar dados compartilhados entre processos.
---

**Modulo_02_Multiprocessamento_07**
- __Compartilhamento de dados em múltiplas processos__
    - O __método Value__ do módulo multiprocessing é usado para criar um valor compartilhado que pode ser acessado e modificado por diferentes processos.

    - O __módulo ctypes__ do Python é uma biblioteca poderosa que permite interagir diretamente com bibliotecas compartilhadas escritas em linguagens como C ou C++, em resumo, ctypes permite definir e manipular estruturas em C ou C++.
---

**Modulo_02_Multiprocessamento_08**
- __Compartilhamento de dados em múltiplas processos__
    - __Lock()__ ou __RLock()__ em Python garante que apenas um __multiprocessing__ por vez execute um bloco específico de código.
            
            Quando usar cada um?
            Use __Lock__:
            Quando o lock será adquirido e liberado apenas uma vez por Thread em cada ciclo.
            
            Use __RLock__:
            Quando uma thread precisa adquirir o lock várias vezes.
---


## Async e Await
- Python: __"async"__ e __"await"__

    -   Em Python, __"async"__ e __"await"__ são palavras-chave que trabalham juntas para habilitar a programação assíncrona (operações de leitura ou escrita em dispositivos IO -
Input/Output). Isso significa que seu programa pode lidar com várias tarefas simultaneamente sem bloquear o __thread__ principal. Isso é particularmente útil para operações vinculadas a solicitações de rede ou acesso ao sistema de arquivos, onde você pode passar muito tempo aguardando.
---

**Modulo_03_Async_01**
- __assicrono_01__:
    - __Função Síncrona__: Executa tarefas uma de cada vez, de forma sequencial. A próxima linha de código só é executada após a conclusão da linha anterior.
    - __Função Assíncrona__: Definição: Permite a execução de várias tarefas de forma "concorrente", utilizando o conceito de event loop. O código não precisa esperar o término de uma tarefa para iniciar outra, podendo pausar e retomar conforme necessário.

- __assicrono_02__:
    - __async def soma_03__:
        - __asyncio.new_event_loop()__: Criando loop de eventos (assíncrono)
        - __.run_until_complete("FUNÇÃO")__: Executa o loop de eventos (assíncrono)
        - __.close()__: Fechando o loop de eventos (assíncrono)
        
    - __async def soma_04__:
        - __asyncio.run("FUNÇÃO")__: Execução de função assíncrona por completo (cria, executar, fechar)
---

**Modulo_03_Async_02**
- __"async e await"__:
    - O __"await"__ só pode ser usado dentro de funções definidas com __"async def"__.

- __Await__ indica que a execução da função será suspensa até que a operação assíncrona que está sendo aguardada seja concluída. Durante esse tempo, o loop de eventos pode executar outras tarefas, permitindo que o programa utilize melhor os recursos.
---

**Modulo_03_Async_03**
---
