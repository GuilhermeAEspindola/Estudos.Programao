a = int(input(' Dígite o primeiro Número: '))
b= int(input(' Dígite o segundo Número:  '))
c = int(input(' Dígite o Terceiro Número: '))
# Verificando o Menor Número 
menor = a
if b < a and b < c:
    menor = b
if c < a and c < a:
    menor = c
print(' O menor valor digitado foi {} '.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c 
print(' O Maior valor digitado foi {} '.format(maior))