"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 8 - Faça um Programa que peça 2 números inteiros e
um número real. Calcule e mostre:
O produto do dobro do primeiro com metade do segundo;
A soma do triplo do primeiro com o terceiro;
O terceiro elevado ao cubo.
Data: 08/09/21
"""
# Entrada de dados
print("------------------------------------------------------------------------")
print("Programa que realiza cálculos com dois números inteiros e um número real")
print("------------------------------------------------------------------------")
print(" ")
print("-Informe os dados exigidos abaixo-")
print(" ")
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = float(input("Digite o número real: "))
print(" ")

# Processamento de dados
produto_dobro1_metade2 = ((numero1*2)*(numero2/2))
soma_triplo1_numero3 = ((numero1*3)+numero3)
cubo3 = (numero3**3)

# Saída de dados
print("----------------------")
print("Resultado dos Cálculos")
print("----------------------")
print(" ")
print("O produto do dobro do primeiro com metade do segundo:", produto_dobro1_metade2)
print("A soma do triplo do primeiro com o terceiro:", soma_triplo1_numero3)
print("O terceiro elevado ao cubo:", cubo3)
