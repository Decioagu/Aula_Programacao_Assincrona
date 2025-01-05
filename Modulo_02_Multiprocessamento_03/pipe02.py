from multiprocessing import Process, Pipe

def carta(conn):
    conn.send("Mensagem do processo filho") # 3º - envia 
    print(conn.recv()) # 6º - Recebe a mensagem do processo pai
    conn.close() # 7º - fechar extremidades da conexão

if __name__ == "__main__":
    pai_conn, filho_conn = Pipe(duplex=True) # 1º - canal de comunicação

    p = Process(target=carta, args=(filho_conn,)) # 2º - executar em paralelo
    p.start() # 2.1º - Inicia o processo
    
    print(pai_conn.recv())  # 4º - Recebe a mensagem do processo filho
    pai_conn.send("Mensagem do processo pai") # 5º - envia para função (carta)
    
    p.join() # 8º - Aguarda o término do processo
