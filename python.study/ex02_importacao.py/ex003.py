from math import hypot
co = float(input("comprimento do cateto oposto: "))
ca = float(input("comprimento do cateto adjacente: "))
hip = hypot(co,ca)
print("A hipotenusa vai medir {:.2f} ".format(hip))

"""from math import sqrt
n1 = float(input("dígite o valor do cateto oposto: "))
n2 = float(input("dígite o valor do cateto adjacente: "))
cal = (n1 ** 2) + (n2 ** 2)
hip = sqrt(cal)
print("a hipotenusa é {:.2f}".format(hip))"""

'''n1 = int(input("digite o  numero: "))
n2 = int(input("digite o numero: "))
cat = (n1 ** 2) + (n2 ** 2)
hip = cat ** (1/2)
print("a hipotenusa é {:.2f}".format(hip))'''

"""co = float(input("comprimento do cateto oposto: "))
   ca = float(input("comprimento do cateto adjacente: "))
   hi = (co ** 2 + ca ** 2) ** (1/2)
   print("A hipotenusa vai medir {:.2f}".format(hi))
"""
