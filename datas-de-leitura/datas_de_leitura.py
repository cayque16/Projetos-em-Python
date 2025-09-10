# -*- coding: utf-8 -*-
from datetime import date,timedelta
import os.path
import json

livro = input("Informe o nome do livro: ")
tipo = int(input('''Informe a forma de marcação:
  1 - Percentual
  2 - Páginas
'''))
paginas = 0
if (tipo == 2):
  paginas = int(input("Informe o numero de paginas: "))

dia,mes,ano = map(int,input("Informe a data de inicio da leitura: ").split("/"))

if ano < 2000:
  ano = '20'+str(ano)
dataInicial = date(int(ano),mes,dia)
startDate = str(ano) + '-' + str(mes).zfill(2) + '-' + str(dia)

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

pasta = "livros/"+str(ano)
indice = 1
print(pasta)
if os.path.isdir(pasta):
  for arquivo in os.listdir(pasta):
    if os.path.isfile(os.path.join(pasta, arquivo)):
      indice += 1
else:
  os.mkdir(pasta)

livro_arq = pasta+"/"+str(indice).zfill(2)+'_'+livro.replace(" ","_")
arquivo = open(livro_arq+'.txt','w')
arquivo.write(result)
arquivo.close()

arquivo_historico = 'livros/historico-geral.json'
with open(arquivo_historico, 'r') as arquivo:
  dados = json.load(arquivo)

novo_livro = {
  "title": livro,
  "startDate": startDate,
  "totalPage": paginas
}

if (int(ano) == (dados['data'][-1]['year'])):
  dados['data'][-1]['books'].append(novo_livro)
else:
  novo_ano = {
    "year": int(ano),
    "books": [novo_livro]
  }

  dados['data'].append(novo_ano)

with open(arquivo_historico, 'w') as arquivo:
  json.dump(dados, arquivo, indent=2)

print(result)
