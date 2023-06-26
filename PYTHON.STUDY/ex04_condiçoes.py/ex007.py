distância = float(input(' Dígite a distância da viagem: '))
print('-=-' * 20)
print('Você está preste a começar uma viagem de {}km'.format(distância))
print('-=-' * 20)
'''if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('o preço da sua viagem será de R$ {} reais'.format(preço))
print('-=-' * 20)'''
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('o preço da sua viagem será de R$ {} reais'.format(preço))
print('-=-' * 20)    