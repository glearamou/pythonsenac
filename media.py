p1 = float(input('Insira a primeira nota: '))
p2 = float(input('Insira a segunda nota: '))
p3 = float(input('Insira a terceira nota: '))

media = (p1+p2+p3)/3

print("Sua média é: ", media)
if (media >= 9):
    print("Ótima média")
elif (media >= 6 and(media<9)):
    print("Média regular")
else:
    print("Média ruim")
