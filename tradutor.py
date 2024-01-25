pt = ['maçã', 'uva', 'abacaxi', 'limão', 'laranja', 'kiwi', 'lichia', 'amora']
ing = ['apple', 'grape', 'pineapple', 'lemon', 'orange', 'kiwi fruit', 'lychee', 'mullberry']
esp = ['manzana','uva', 'piña', 'limón', 'naranja', 'kiwi', 'lichi', 'mora']
fra = ['pomme', 'raisin', 'ananas', 'citron', 'orange', 'kiwi', 'litchi', 'mûrier']

print(f'{pt}\nEscolha um número entre 0 e 7, sendo 0 para maçã, 1 para uva e assim por diante até o 7 - amora')
resp = int(input('Selecione um valor entre 1 e 8:'))

print(f'Português: {pt[resp]}\nInglês: {ing[resp]}\nEspanhol:{esp[resp]}\nFrancês:{fra[resp]}')