import json
import requests

data = '''
    {
        "codigo": "1",
        "primeiroNome": "Joao",
        "ultimoNome": "Smith",
        "idade": 25,
        "endereco": {
            "rua": "Rua Assis Brasil, 1000",
            "cidade": "Blumenau",
            "estado": "SC"
        },
        "telefones": [
            "5555-5555",
            "9999-9999"
        ],
        "emails": [
            {
                "tipo": "pessoal",
                "endereco": "joao@joao.com"
            },
            {
                "tipo": "profissional",
                "endereco": "joao.smith@algumaempresa.com"
            }
        ]
    }
'''
'''
#converte de string para json
json_data = json.loads(data)

if json_data['codigo'] == '1':
    print("Codigo: "+json_data['codigo'])
    print("Nome: "+json_data['primeiroNome'] + " " +json_data['ultimoNome'])
    print("Reside na "+json_data['endereco']['rua']+" - "+json_data['endereco']['cidade']+" / "+json_data['endereco']['estado'])
'''

#faz a requisição e guarda a url dentro da variavel response
response = requests.get('https://swapi.co/api/people/')

#metodo json.loads irá converter a url de string para json pegando seu conteudo
json_data = json.loads(response.content)

#primeiro laço irá percorrer os objetos dentro de results
for person in json_data['results']:
    #segundo laço irá percorrer chave e valor
    for k,v in person.items():
        if k == 'name':
            print(k+": "+v)