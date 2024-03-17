base1 = int(input("Dígite o Comprimento do Primeiro Retângulo: "))
altura1 = int(input("Dígite o Altura do Primeiro Retângulo: "))
base2 = int(input("Dígite o Comprimento do Segundo Retângulo: "))
altura2 = int(input("Dígite o Altura do Segundo Retângulo: "))
a1 = base1 * altura1
a2 = base2 * base2
aT = a1 + a2
print("A Área do Primeiro Retângulo é: {}cm²".format(a1))
print("A Área do Segundo Retângulo é: {}cm²".format(a2))
print("A Área Total dos Retângulos é: {}cm²".format(aT))