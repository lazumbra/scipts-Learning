import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["jeffer@gmail.com", "vera@gmail.com"],
            "has_licese": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}

'''

data = json.loads(people_string)
print(data)

# Pegar todos os elementos do json
for person in data['people']:
    print(person)
    #Caso eu queira pegar apenas os nomes das pessoas
    print(person['name'])

#Caso eu queira deletar um elemento do meu json
for person in data['people']:
    del person['phone']

#Converter de Json ou dicionario para string
new_string = json.dumps(data)
print(new_string)

#Caso queira converter o json para string e ainda
# identar pra fica mais legível de ler
new_string = json.dumps(data, indent=2)

print(new_string)

#Caso queira além de converter para string, fazer um
# sort das keys. Basta fazer:
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)
