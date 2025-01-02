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

**Modulo_Threadds_04**
banco_inseguro.py:
- Neste exemplo existe conflito entre múltiplas Threads onde as operações de serviços "Transferência" ocorre de maneira simultânea, ocasionando erro de valores __("race conditions")__, pois as Threads compartilham o mesmo recurso (objeto).

banco_seguro.py:
- Neste exemplo foi eliminado o conflito de múltiplas Threads com o uso de Rlock(), função garantidora que apenas uma thread por vez execute um bloco específico de código, preservando a consistência do recurso ou objeto.
---

**Modulo_Threadds_05**
---




## Async  e Await
- Python: __"async"__ e __"await"__

    -   Em Python, __"async"__ e __"await"__ são palavras-chave que trabalham juntas para habilitar a programação assíncrona. Isso significa que seu programa pode lidar com várias tarefas simultaneamente sem bloquear o __thread__ principal. Isso é particularmente útil para operações vinculadas a solicitações de rede ou acesso ao sistema de arquivos, onde você pode passar muito tempo aguardando.
---