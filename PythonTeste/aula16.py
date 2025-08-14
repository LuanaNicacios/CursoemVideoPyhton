#AULA VARIÁVEIS COMPOSTAS - 'TUPLAS'
#TUPLAS SÃO IMUTÁVEIS

'''
TUPLAS = ()
LISTAS = []
DICIONARIO = {}
'''

'''
pessoas = ('LUANA', 24, 'F', 52)
print(pessoas)
Vai mostrar todas as informações acima sem problemas, pos no python pode ter dados de diferentes tipos na mesma variavel,
dentro das tuplas.
del(pessoa)
Deleta a tupla inteira. 
'''

'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
A Tupla C vai juntar as variaveis A e B
print(len(c))
conta quantos elementos tem dentro de C
print(c.count(5))
Mostra quantas vezes aparece o número 5 (elemento), dentro de C
print(c.index(8))
Mostra em que posição está um elemento. 
print(c.index(5, 1))
Vai mostar a posição onde segundo 5 está pos pulou a posição 0 que é a do primeiro 5(Deslocamento). 
'''

'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'Batata Frita')
print(sorted(lanche))
Sorted coloca a lista em ordem.
'''

'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('COMI MUITO!')
'''


'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'Batata Frita')
for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posiçao {posicao}')
print('COMI MUITO!')
'''


'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim'):
    print(len(lanche))
mostra a quantidade de itens que a dentro da variavel lanche
'''

'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print(f'COMI MUITO!')
'''


'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche)
vai mostar todos os nomes dentro da variavel lanche.
'''

'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[1])
vai mostar apenas o lanche que está na posição 1 que é o Suco.
'''

'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[-2])
vai mostar a pizza, pos está na 2 posição de trás para frente.
'''

'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[1:3])
O elemento 3 não vai ser mostrado pos no fatiamento ele desconsidera o ultimo elemento
'''

'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[2:])
Vai mostrar do lache que esta na posição 2 que é a pizza até a ultima posição que é o pudim.
'''

'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[:2])
Vai mostrar o inicio, até a posição suco, pos no fatiamente ele desconsidera o ultimo elemento que seria o suco.
'''

'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[-2:])
Vai começar na pizza e vai até o final, em ordem decrescente.
'''

