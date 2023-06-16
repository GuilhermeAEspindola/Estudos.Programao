from random import randint # biblioteca do python que utilizei para gerar número aleatório.
from time import sleep
n = int(input(' digite o numero que pensei: ')) # o usuário era digitar o número.
print( '-=-' * 20) # para fazer linhas do seu gosto no terminal. 
computador = randint(0,5) # comando que ira gerar o numero aleatório no terminal 
print('processando...')
sleep(2)
print( ' o número que pensei foi {} '.format(computador)) # será mostrado o numero aleatório.
print( '-=-' * 20 )

if  n == computador: # se for igual a o computador lera o print.
    print( ' parabéns voce acertou o numero que pensei! ')
    print('-=-' * 20)
else: # senão lera esse print.
    print(' não foi dessa vez! ')

