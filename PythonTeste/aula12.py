#MUNDO 2 PYTHON - AULA 12 - CRIAR OUTRO REPOSITORIO PARA SUBIR#
nome = str(input('Digite seu nome? ')).upper()
if nome == 'LUNA':
    print('Que nome lindo você tem!')
elif nome == 'JOSE' or nome == 'MARIA' or nome == 'JOAO':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'ANA, CLAUDIA, JESSICA, JULIANA':
    print('Que belo nome feminino você tem!')
else:
    print('Seu nome é bem comum.')
print('Tenha um bom dia, {}!'.format(nome))

#O elif não funciona com nomes com acentos, ele vai para o else.#