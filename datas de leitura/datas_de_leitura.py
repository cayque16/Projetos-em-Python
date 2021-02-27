# -*- coding: utf-8 -*-
from datetime import date,timedelta

livro = input("Informe o nome do livro: ")
tipo = int(input('''Informe a forma de marcação:
  
  {1}--Percentual
  {2}--Páginas

'''))
if (tipo == 2):
  paginas = int(input("Informe o numero de paginas: "))

dia,mes,ano = map(int,input("Informe a data de inicio da leitura: ").split("/"))
dataInicial = date(ano,mes,dia)
resto = 0
if (tipo != 2):
  porcent = 5
  simbolo = '%'
else:
  porcent = paginas // 20
  resto = paginas % 20
  simbolo = ''
result = ""
total = 0

for i in range(1,21):
  temp = porcent
  if(resto > 0 and tipo == 2):
    porcent += 1
    resto -= 1
  if(tipo != 2):
    total = porcent
  else:
    total += porcent
  valor = "0"+str(total) if total < 10 else total
  porcent = temp
  result += "{}: {}{}".format(dataInicial.strftime('%d/%m/%Y'),valor,simbolo)
  if(i%4==0):
    result += "\n"
  else:
    result += " | "
  dataInicial += timedelta(days=1)
  if(tipo != 2):
    porcent += 5

livro = "/var/www/Projetos-em-Python/datas de leitura/livros/" + livro.replace(" ","_")
arquivo = open(livro+'.txt','w')
arquivo.write(result)
arquivo.close()

print(result)
