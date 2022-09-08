from math import radians, sin, cos, tan
ang = float(input("digite o valor do ângulo: "))
soh = sin(radians(ang))
cah = cos(radians(ang))
toa = tan(radians(ang))
print("o ângulo de {} tem o seno de {:.2f}".format(ang,soh))
print("o ângulo de {} tem o cosseno de {:.2f}".format(ang,cah))
print("o ângulo de {} tem o tangente de {:.2f}".format(ang,toa))
