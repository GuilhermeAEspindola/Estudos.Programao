salario = float(input(' Dígite o valor do seu Salário? R$ '))
'''aumento =  ((salario * 10) / 100) + salario
aumento1 = ((salario * 15) / 100) + salario
if salario >= 1250:
    print(' O Seu Reajuste Salarial será de: R${:.2f} reais '.format(aumento))
else:
    print(' O Seu Reajuste Salarial será de: R${:.2f} reais '.format(aumento1))''' 
if salario <= 1250:
    aumento =  salario + (salario * 15 / 100) 
    print(' O Seu Reajuste salarial sera de R$ {:.2f} reais'.format(aumento))
else:
    aumento =  salario + (salario * 10 / 100) 
    print('O seu Reajuste   salarial sera de R$ {:.2f} reais '.format(aumento))
