from datetime import date
from time import sleep
ano = int(input('Dígite o ano para saber se ele e BISSEXTO: '))
print(' PROCESSANDO... ')
print(sleep(1))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print(' O ANO de {} é BISSEXTO! '.format(ano))
else:
    print(' O ANO de {} não é BISSEXTO! '.format(ano))