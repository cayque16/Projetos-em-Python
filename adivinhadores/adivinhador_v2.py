from random import randint
print("Pense em um numero.")
min = int(input("Agora me fale qual valor minimo do intervalo onde se encontra o seu numero: "))
max = int(input("Agora me fale qual valor maximo do intervalo onde se encontra o seu numero: "))

chute = int((max + min)/2)
while True:
    print("Acho que voce pensou no {}".format(chute))
    print('''Eu acertei?!
        [1] SIM
        [2] NAO, MEU NUMERO E MAIOR
        [3] NAO, MEU NUMERO E MENOR
    ''')
    resposta = int(input())
    if resposta == 1:
        print("SHOW DE BOLA!!!!")
        break
    elif resposta == 2:
        min = chute
    elif resposta == 3:
        max = chute
    chute = int((max + min)/2)