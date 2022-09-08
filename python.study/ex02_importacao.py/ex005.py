from glob import escape
from random import choice
a1 = input("dígite o nome do primeiro aluno: ")
a2 = input("dígite o nome do segundo aluno: ")
a3 = input("dígite o nome do terceiro aluno: ")
a4 = input("dígite o nome do quarto aluno: ")
lista = [a1,a2,a3,a4]
escolhido = (choice(lista))
print("o aluno escolhido foi {}".format(escolhido))