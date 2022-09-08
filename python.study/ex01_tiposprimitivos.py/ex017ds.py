n = float(input("dígite o valor da compra: R$"))
d = float(input("digite o valor do desconto: "))
des = (d * n) / 100
vlr = des - n
acr = des + n
print("o valor de R${:.2f}, com desconto de  {:.0f}%,  seria de R${:.2f}, então ficaria o valor final de R${:.2f}. ".format(n,d,des,vlr))
print("Acréscimo ficaria no valor de R${:.2f}. ".format(acr))