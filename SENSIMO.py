import random

sensimo = r"""
  ^~^  ,
 (-Y-) )
 /   \/
(\|||/) 
"""

sensimo2 = r"""
  ^~^  ,
 ('Y') )
 /   \/
(\|||/) 
"""
def guess_the_number():
    secret_number = random.randint(1, 100)
    guess = 0
    attempts = 0
    print("Bem vindo ao jogo de adivinha do Sensimo!")
    print(sensimo)
    print("Ele escolheu um número entre 1 e 100. Tente adivinhar o número para que ele acorde!")

    while guess != secret_number:
        try:
            guess = int(input("Adivinhe: "))
            attempts += 1

            if guess < secret_number:
                print("Muito baixo! Tente novamente.")
            elif guess > secret_number:
                print("Muito alto! Tente novamente.")
            else:
                print(sensimo2)
                print(f"Parabéns! Você adivinhou o número secreto {secret_number} em {attempts} tentativas!")
        except ValueError:
            print("Erro! Sensimo só ouve números. Tente novamente.")

if __name__ == "__main__":
    guess_the_number()
