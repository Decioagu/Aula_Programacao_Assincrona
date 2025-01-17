from multiprocessing import Process, Pipe


def ping(conn):
    conn.send('Décio') # extremidade de envio

def pong(conn):
    msg = conn.recv() # extremidade de recepção
    print(f'{msg} Santana')

def main():
    # duplex=True: permitindo que ambos os extremos do pipe possam enviar e receber dados.
    conn1, conn2 = Pipe(duplex=True)

    # Cada extremidade pode usar os métodos send() para enviar e recv() para receber dados.
    p1 = Process(target=ping, args=(conn1,))
    p2 = Process(target=pong, args=(conn2,))

    p1.start() # Inicia o processo
    p2.start() # Inicia o processo

    p1.join() # Aguarda o término do processo
    p2.join() # Aguarda o término do processo

if __name__ == '__main__':
    main()
