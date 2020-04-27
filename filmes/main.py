import requests, json

imdbid = input("Informe o ImdbID do filme: ")

key = ???

params = {'i': imdbid,'apikey': key}
reque = requests.get('http://www.omdbapi.com/',params=params)

result = json.loads(reque.text)

print("Titulo: "+result['Title'])
print("Ano: "+result['Year'])
print("Duracao: "+result['Runtime'])
print("Nota IMDB: "+result['imdbRating'])