import requests

resp = requests.get('https://api.hgbrasil.com/weather?woeid=455908')
dados = resp.json()
print(dados['results']['forecast'])