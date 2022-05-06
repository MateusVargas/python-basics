import requests

resposta = requests.get('https://ipapi.co/json')
dados = resposta.json()

print('Endereço IP: {}'.format(dados['ip']))
print('Cidade: {}'.format(dados['city']))
