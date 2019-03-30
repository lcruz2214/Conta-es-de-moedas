import requests
import time
import json



url = "http://data.fixer.io/api/latest?access_key=c94d452d1c117229f0977f5cb424731d" # consumindo uma api da internet

print("Acessando base de dados . . .")
response = requests.get(url) # aqui obtem o objeto request
if response.status_code == 200:
    print("Acesso com sucesso")
    time.sleep(1)
    print("buscando info das moedas")
    dados = response.json() # 
    print("Euro: {:.2f}".format(dados["rates"]["EUR"]))
    print("Dolar x Real {:.2f}".format(dados["rates"]["BRL"] / dados["rates"]["USD"]))
    print("Dolar: {:.2f}".format(dados["rates"]["USD"]))
    print("Bitcoin: {:.2f}".format(dados["rates"]["BTC"]))

