n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))
n4 = float(input("digite a quarta nota: "))
ma = (n1+n2+n3+n4) / 4 
print("a média aritmética do aluno é: {:.1f}!".format(ma))
print("aluno aprovado! {}".format(ma >= 5))
print("aluno reprovado! {}".format(ma < 5))