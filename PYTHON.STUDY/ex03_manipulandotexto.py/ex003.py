from locale import delocalize


n1 = int(input("Dígite um número: "))
uni = n1 // 1 % 10
dez = n1 // 10 % 10
cen = n1 // 100 % 10
mil = n1 // 1000 % 10
print("O Número {}".format(n1))
print("Tem a Unidade {}.".format(uni))
print("A Dezena é {}.".format(dez))
print("A Centena é {}".format(cen))
print("A Milhar é {}".format(mil))