from multiprocessing import Value
import ctypes

# Criando um valor compartilhado do tipo booleano
status = Value(ctypes.c_bool, False) # 1º

# Exemplo de como usar
def altera_status(valor):# 3.1º
    with status.get_lock():  # Garantindo troca de valor devido o uso de "multiprocessing" (bloqueio)
        status.value = valor

# Lendo o valor
print("Status inicial:", status.value)  # 2º - False

# Alterando o valor
altera_status(True) # 3º
print("Status alterado:", status.value)  # 4º -True
