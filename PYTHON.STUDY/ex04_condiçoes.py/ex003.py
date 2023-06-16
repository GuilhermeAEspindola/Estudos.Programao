nota1 = float(input(' digite sua primeira nota: '))
nota2 = float(input(' digite sua segunda nota: '))
m = ( nota1 + nota2 ) / 2
print(" sua média foi : {:.1f} ".format(m))
if  m>=5:
    print('sua nota foi boa!')
else:
    print('sua nota foi ruim')
print('---fim---')