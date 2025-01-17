# Criando um valor tipo booleano
status = False # 1º

# Exemplo de como usar
def altera_status(valor):# 3.1º
    # global status # função com valor global
    status= valor

# Lendo o valor
print("Status inicial:", status)  # 2º - False

# Alterando o valor
altera_status(True) # 3º
print("Status alterado:", status)  # 4º -True
