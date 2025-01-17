import threading
import time

def processar():
    print('[', end='', flush=True)
    for _ in range(1, 11):
        print('#', end='', flush=True)
        time.sleep(1)
    print(']', end='', flush=True)

if __name__ == '__main__':
    # Marcando o início
    inicio_time = time.time()

    ex = threading.Thread(target=processar) ### Thread
    ex.start()
    ex.join()

    # Marcando o fim
    fim_time = time.time()

    # Calculando o tempo decorrido
    tempo = fim_time - inicio_time

    print(f"\nTempo de execução: {tempo:.2f} segundos")


