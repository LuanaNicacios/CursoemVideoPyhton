
nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('Seu nome em Minúscula é: {}'.format(nome.lower()))
print('seu nome em Maiúscula é: {} '.format(nome.upper()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))



