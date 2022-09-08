from glob import glob1
from random import shuffle
"""sorteio para o trabalho"""
g1 = input("dígite o nome do primeiro grupo: ")
g2 = input("dígite o nome do segundo grupo: ")
g3 = input("dígite o nome do terceiro grupo: ")
g4 = input("dígite o nome do quarto grupo: ")
lista = [g1,g2,g3,g4]
ordem = (shuffle(lista))
print("a ordem dos grupos sera de {}".format(lista))
print("-".join(lista))