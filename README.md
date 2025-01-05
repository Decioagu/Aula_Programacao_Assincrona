# Aula_Programacao_Assincrona
 Programação Concorrente e Assíncrona com Python

## Threads
- Em Python, __threads__ são linhas de execução concorrentes em um mesmo processo. Elas são concorrentes no sentido de que executam simultaneamente. Isso pode ser útil para melhorar o desempenho de um programa, pois __permite que ele execute múltiplas tarefas ao mesmo tempo__.
---

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

- __multiprocessing.current_process().name__: é usada para obter o nome do processo atual em execução.
- __Process(target=???, args=(???,), name='???')__:
    - __Thread()__:  classe do módulo __multiprocessing__ que permite criar e gerenciar execução paralela de código
    - __target()__: define a função que será executada pela thread
    - __args()__: argumentos passados em forma de tupla para função
    - __name()__: define um nome para o processo
- __.start()__: # Inicia o processo
- __.join()__: # Aguarda o término do processo
---

**Modulo_02_Multiprocessamento_02**
- __pool = multiprocessing.Pool()__: gerenciar tarefas para os processos disponíveis de forma eficiente permite executar tarefas em paralelo utilizando múltiplos processos, aproveitando os vários núcleos disponíveis no processador. Possibilitado ao programador manipular a quantidade de processos a ser executado. 
- __pool.close()__: Fecha o pool para novas tarefas
- __pool.join()__: Aguarda os processos finalizarem
---

**Modulo_02_Multiprocessamento_03**
- __Compartilhamento de dados em múltiplas processos__
    - O __método multiprocessing.Pipe()__ cria um canal de comunicação (pipe) __entre dois processos__ que pode ser usado para trocar dados. Esse método retorna um par de conexões (duas extremidades do pipe) que permitem que os processos se comuniquem entre si.
---

**Modulo_02_Multiprocessamento_04**
- __Compartilhamento de dados em múltiplas processos__
    - O __Queue é uma classe do módulo queue__ em Python, usada para implementar estruturas de fila. Filas são coleções ordenadas, onde o primeiro elemento inserido é o primeiro a ser removido. Essa classe é frequentemente utilizada em cenários de multithreading para gerenciar dados compartilhados entre processos.
---

**Modulo_02_Multiprocessamento_05**
- __Compartilhamento de dados em múltiplas processos__
    - O __método Value__ do módulo multiprocessing é usado para criar um valor compartilhado que pode ser acessado e modificado por diferentes processos.

    - O __módulo ctypes__ do Python é uma biblioteca poderosa que permite interagir diretamente com bibliotecas compartilhadas escritas em linguagens como C ou C++, em resumo, ctypes permite definir e manipular estruturas em C ou C++.
---

**Modulo_02_Multiprocessamento_06**


## Async  e Await
- Python: __"async"__ e __"await"__

    -   Em Python, __"async"__ e __"await"__ são palavras-chave que trabalham juntas para habilitar a programação assíncrona. Isso significa que seu programa pode lidar com várias tarefas simultaneamente sem bloquear o __thread__ principal. Isso é particularmente útil para operações vinculadas a solicitações de rede ou acesso ao sistema de arquivos, onde você pode passar muito tempo aguardando.
---