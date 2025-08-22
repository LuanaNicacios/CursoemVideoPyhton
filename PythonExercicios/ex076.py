produtos = ('café', 4.50,
            'leite', 1.50,
            'arroz', 3,
            'feijão', 4,
            'macarrão', 2,
            'cuscuz', 0.50,
            'tapioca', 1,
            'farofa', 1.99,
            'pão', 2.99)
print('_'* 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('_'* 30)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<20}', end='')
    else:
        print(f'R${produtos[pos]:>5.2f}')
print('_'* 30)