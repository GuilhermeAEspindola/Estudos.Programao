sa = float(input("dígite o sálario do funcíonario: R$"))
po = int(input("digite o valor do aumento: %"))
au = sa + (sa * po / 100)
print("o sálario do funcíonario é de R${:.2f}, com o aumento de {:.2f}% passará a ficar no valor de R${:.2f}.".format(sa,po,au))