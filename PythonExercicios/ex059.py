from time import sleep
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] Somar \n'
      '[ 2 ] Multiplicar \n'
      '[ 3 ] Maior \n'
      '[ 4 ] Novos Números \n'
      '[ 5 ] Sair')
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        soma = valor1 + valor2
        print('A soma entre {} e {} é: {} '.format(valor1, valor2, soma))
    elif opcao == 2:
        multiplicar = valor1 * valor2
        print('A multiplicação entre {} e {} é: {} '.format(valor1, valor2, multiplicar))
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('Entre {} e {} o maior valor é: {} '.format(valor1, valor2, maior))
    elif opcao == 4:
        print('Informe os números novamente.')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida tente novamente.')
    print('=-='*10)
    sleep(2)
print('Fim do programa! Volte sempre!')


