import random
import time

while True:
    D = input("Escolha a dificuldade (facil, normal, dificil): ")

    if D == "facil":
        DT = 15
        break
    elif D == "normal":
        DT = 30
        break
    elif D == "dificil":
        DT = 45
        break
    else:
        print("Opção inválida. Escolha entre 'facil', 'normal' ou 'dificil'.")

S = random.randint(1, 100)

T = time.time()

while True:
    Ta = time.time()
    if Ta - T > DT:
        print("Acabou o tempo! Você perdeu!")
        break

    try:
        E = int(input("Escolha um número entre 1 e 100: "))

        if E < 1 or E > 100:
            print("Por favor, escolha um número dentro do intervalo de 1 a 100.")
            continue

        if E < S:
            print("É maior!")
        elif E > S:
            print("É menor!")
        else:
            print("Parabéns! Você acertou o número!")
            break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
