# -*- coding: utf-8 -*-
from datetime import date,timedelta

livro = input("Informe o nome do livro: ")
dia,mes,ano = map(int,input("Informe a data de inicio da leitura: ").split("/"))
dataInicial = date(ano,mes,dia)
porcent = 5
result = ""

for i in range(1,21):
  result += "{}: {}%".format(dataInicial.strftime('%d/%m/%Y'),"05" if porcent == 5 else porcent)
  if(i%4==0):
    result += "\n"
  else:
    result += " | "
  dataInicial += timedelta(days=1)
  porcent += 5

livro = "livros/" + livro.replace(" ","_")
arquivo = open(livro+'.txt','w')
arquivo.write(result)
arquivo.close()

print(result)
