diametro = float(input("Dígite o Valor do Diâmetro Para descobrirmos o Raio do Cilindro: "))
Altura = float(input("Dígite a Altura do Cilindro: "))
raio = diametro / 2
ab = 3.14 * raio ** 2
vol = Altura * 3.14 * raio**2
print("O Raio do Cilindro é: {}cm²".format(raio))
print("A Área da Base do Cilindro é: {}cm²".format(ab))
print("O Volume do Cilindro é: {:.2f}cm²".format(vol))