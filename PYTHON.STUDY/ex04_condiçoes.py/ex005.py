from time import sleep
carro = float(input(' dígite a velocidade que estava o carro: '))
multa =  (carro - 80) * 7
print('PROCESSANDO...')
sleep(2)
if carro < 80:
     print('Você esta a {}km por hora.'.format(carro))
     print('-=-' * 20)
     print(' está na velocidade correta! ')
     print('-=-' * 20)
else:
     print('Você esta a {}km por hora.'.format(carro))
     print('-=-' * 20)
     print(' está na velocidade incorreta! ')
     print('Será multado em R${:.2f} reais'.format(multa))
     print('-=-' * 20)