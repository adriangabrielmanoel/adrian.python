import random

def adivinha_numero():
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    print("jogo do adrian!")
    print("Tente adivinhar um número entre 1 e 10")

    while True:
        palpite = input("Digite seu palpite (ou 'kitar' ): ")
        if palpite.lower() == 'kitar':
            print("Obrigado por jogar")
            break
        tentativas += 1
        try:
            palpite = int(palpite)
            if palpite < 1 or palpite > 10:
                print(" digite um número entre 1 e 10.")
                continue
            
            if palpite < numero_secreto:
                print("Muito baixo! ")
            elif palpite > numero_secreto:
                print("Muito alto! ")
            else:
                print("Parabéns! Você adivinhou  {numero_secreto} em {tentativas} tentativas")
                break
        except ValueError:
            print(" insira um valor")

adivinha_numero()