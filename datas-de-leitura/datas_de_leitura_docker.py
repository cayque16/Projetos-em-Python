# -*- coding: utf-8 -*-
from datetime import date,timedelta
import os.path

livro = input("Informe o nome do livro: ")
tipo = int(input('''Informe a forma de marcação:
  1 - Percentual
  2 - Páginas
'''))
if (tipo == 2):
  paginas = int(input("Informe o numero de paginas: "))

dia,mes,ano = map(int,input("Informe a data de inicio da leitura: ").split("/"))

if ano < 2000:
  ano = '20'+str(ano)
dataInicial = date(int(ano),mes,dia)

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
  valor = str(total).zfill(2)
  porcent = temp
  result += "{}: {}{}".format(dataInicial.strftime('%d/%m/%Y'),valor,simbolo)
  if(i%4==0):
    result += "\n"
  else:
    result += " | "
  dataInicial += timedelta(days=1)
  if(tipo != 2):
    porcent += 5

pasta = "Projetos-em-Python/datas-de-leitura/livros/"+str(ano)
indice = 1
print(pasta)
if os.path.isdir(pasta):
  for arquivo in os.listdir(pasta):
    if os.path.isfile(os.path.join(pasta, arquivo)):
      indice += 1
else:
  os.mkdir(pasta)

livro = pasta+"/"+str(indice).zfill(2)+'_'+livro.replace(" ","_")
arquivo = open(livro+'.txt','w')
arquivo.write(result)
arquivo.close()

print(result)
