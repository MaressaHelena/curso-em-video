# O exercicio corresponde a aula 7 do CURSO EM VÍDEO.


# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Valor atual: '))
desconto = (produto - (produto*0.05))
print(f'Valor com 5% de desconto: {desconto}')
print('fim')
