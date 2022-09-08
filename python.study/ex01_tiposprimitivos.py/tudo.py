n1 = int(input("dígite um número: "))
n2 = int(input("digite um número: "))
a = n1 + n2
s = n1 - n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
rd = n1 % n2
po = n1 ** n2
rz = (n1 + n2)**(1/2)
rc = (n1 + n2)**(1/3)
print("os resultados são: {}\n{}\n{}\n{}\n{}\n{}\n{}\n{:.3f}\n{:.2f}!".format(a,s,d,m,di,rd,po,rz,rc))
#/tipos primitivos/
# para quebra a linha vc coloca \n aonde você quer que ala quebre.
# e se você quiser "juntar as linhas", ou seja um print com outro print utlize end=""com nada dentro das aspas"".
# para fazer raíz quadrada utilize potênciaçâo ** (1/2).
# e se quiser raíz cubíca você utliza potênciação ** (1/3).
# sinal de igual em python é ==.
# ordem de precedência 1. ;(); 2. ;**; 3. ;*;  ;/;  ;//;  ;%; 4. ;-; ;+;
# dentro das chaves {}.format eu posso  colocar caractéres com {:3...}, posso usar alinhamentos para a direita {:>3...},
# e também para a esqueda {:<3...}, ou posso usar o circunflexo para alinhar no centro {:^3...}.
# posso também colocar qualquer sinal dentro das chaves {:=^3;...}, que ele vai repetir dependendo do número que você colocar.
# {:.2f}!".format - o  {:.2f} serve para você formatar números que ficam grandes nas operações arítmeticas.ex: 4,686868 ficará, 4,68.
# # também posso fazer da seguinte forma sem precisar criar  várias váriaveis no programa, ex:
# print("analisando o valor {}, o sucessor é {}, e seu antecessor é {}".format(n,(n-1),(n-2)))
# pow(n,(1/2)) também cálcula a raíz quadrada.
#       