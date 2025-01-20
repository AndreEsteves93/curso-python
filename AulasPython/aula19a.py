pessoas = {'nome': 'Andre', 'sexo': 'M', 'idade': 31}
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
# del pessoas['sexo']
pessoas['nome'] = 'Jão'
pessoas['peso'] = 90
print(pessoas['nome'])
print(pessoas)
