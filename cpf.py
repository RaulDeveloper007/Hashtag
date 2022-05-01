cpf = input('Digite o número de seu CPF: ')
cpf = cpf.strip()
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')
print(len(cpf))
if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print('Digite seu CPF corretamente. Digite apenas números.')

