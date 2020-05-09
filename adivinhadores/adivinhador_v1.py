from random import randint

alvo = randint(0,1000)
tentativas = 1
entrada = int(input("Entre com um numero (0,1000): "))
while entrada != alvo:
  tentativas += 1
  if (entrada < alvo):
    entrada = int(input("Digite um numero maior: "))
  else:
    entrada = int(input("Digite um numero menor: "))
print("Parabens, voce acertou, com {} tentativa(s)".format(tentativas))