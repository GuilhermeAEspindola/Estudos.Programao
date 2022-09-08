real = float(input("digite o valor: "))
print("=" * 12)
dolar = real / 5.17
euro = real / 5.29
print("o valor em Reais é: R${}.\no valor em dólar é: US${:.2f}.\no valor em euro é: €${:.2f}.".format(real,dolar,euro))
print("=" * 12)