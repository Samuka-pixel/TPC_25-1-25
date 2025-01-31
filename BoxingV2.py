import random
import string

def gk():
    """Gera três teclas adjacentes com danos diferentes"""
    i = random.randint(0, len(string.ascii_uppercase) - 3)
    K = string.ascii_uppercase[i:i+3]
    D = [0.2, 0.4, 0.6]
    return dict(zip(K, D))

vida1, vida2 = 10.0, 10.0

while vida1 > 0 and vida2 > 0:
    KD = gk()
    print("\nTeclas disponíveis:", KD)

    A = input("Jogador 1, ataque: ").upper()
    if A in KD:
        vida2 -= KD[A]

    if vida2 <= 0:
        print("Jogador 1 venceu!")
        break

    A = input("Jogador 2, ataque: ").upper()
    if A in KD:
        vida1 -= KD[A]

    if vida1 <= 0:
        print("Jogador 2 venceu!")

    print(f"Vida: Jogador 1 = {vida1:.1f} | Jogador 2 = {vida2:.1f}")
