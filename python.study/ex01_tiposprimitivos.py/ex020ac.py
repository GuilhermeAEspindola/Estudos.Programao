alu = int(input("quantas dias alugados? "))
km = float(input("quantos km rodados "))
car = (alu * 60) + (km * 0.15)

print("o total a pagar é de R${:;2f} ".format(car))
