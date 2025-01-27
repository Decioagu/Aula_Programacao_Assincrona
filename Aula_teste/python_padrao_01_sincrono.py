from datetime import datetime
import math

### Tempo de processamento ###

def main():
    inicio = datetime.now() # tempo inicial

    computar(fim=50_000_000) # processamento da (Função)

    tempo = datetime.now() - inicio # tempo final

    print(f"Terminou em {tempo.total_seconds():.2f} segundos.") # informa tempo utilizado pela (Função)


# (Função) processo de calculo matemático
def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == '__main__':
    main()


"""
Terminou em 16.54 segundos.
"""
