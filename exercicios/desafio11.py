# O exercicio corresponde a aula 7 do CURSO EM VÍDEO.


# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²


largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
area = largura * altura
tinta = area/2
print(f'Dimensões: {largura} x {altura}')
print(f'Área: {area}')
print(f'Tinta em litros para pintar a parede: {tinta}L')
print('FIM')
