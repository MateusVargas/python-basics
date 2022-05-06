# é preciso ter o 'pip' instalado: sudo apt install python-pip
# para trabalhar com requisições HTTP: pip install requests

#REQUISIÇÃO HTTP
import requests

resposta = requests.get('https://viacep.com.br/ws/97095540/json/')
print('Código http da resposta: ',resposta.status_code)
dados = resposta.json()

print('Seu Bairro: {}'.format(dados['bairro']))
print('Sua Rua: {}'.format(dados['logradouro']))
