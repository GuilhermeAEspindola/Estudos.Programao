med1 = str(input("Digite o Nome do primeiro Medicamento: "))
val1 = float(input("Digite o Valor do primeiro Medicamento: "))
med2 = str(input("Digite o Nome do Segundo Medicamento: "))
val2 = float(input("Digite o Valor do Segundo Medicamento: "))
valT = val1 + val2
print("O Nome do primeiro Medicamento é: {}.\nO Valor dele é: R$ {} Reais. ".format(med1,val1))
print("O Nome do Segundo Medicamento é {}.\nO Valor dele é: R$ {} Reais. ".format(med2,val2))
print("O Valor Total Do Pedido é de: R$ {} Reais.".format(valT))