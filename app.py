import random

# Define o número secreto
numero_secreto = random.randint(1, 100)

# Inicia o jogo
while True:
    chute = input("Digite um número entre 1 e 100: ")
    
    # Verifica se a entrada é um número válido
    if not chute.isdigit():
        print("Por favor, digite um número válido.")
        continue
    
    chute = int(chute)
    
    if chute < numero_secreto:
        print("Mais alto!")
    elif chute > numero_secreto:
        print("Mais baixo!")
    else:
        print("Parabéns! Você adivinhou o número secreto!")
        break
