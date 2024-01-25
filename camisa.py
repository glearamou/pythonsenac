inicio = str(input('Deseja começar?\nS - SIM \nN - NÃO \nOpção: '))

while inicio == str('S'):
    nome = str(input('Nome da pessoa: '))
    cor = str(input('Cor da camisa: '))

    print(f'A camisa do(a) {nome} é {cor}')
    inicio = str(input('Deseja começar?\nS - SIM \nN - NÃO \nOpção: '))