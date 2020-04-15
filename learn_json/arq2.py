import json

# Como ler um arquivo JSON
with open( 'states.json') as f:
    data = json.load(f)

#Caso queira pegar os nomes e as abreviações. Fazer o 
# seguinte
for state in data['states']:
    print(state['name'], state['abbreviation'])

# Veja como deletar chaves do seu json
for state in data['states']:
    del state['area_codes']

#salvar de um JSON para arquivo
with open('new_states.json', 'w') as f:
    json.dump(data, f)

#caso queira salvar identado
with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)