altura = float(input("Qual é a Altura ? "))
largura = float(input("Qual é a Largura ? "))
área = largura * altura 
print("Com {}m de Altura e {}m de Largura você tem uma Área de {}m².".format(altura,largura,área))
tin = área / 2
print("E com {}m², você consegue pintar uma Área de {}l.".format(área,tin))