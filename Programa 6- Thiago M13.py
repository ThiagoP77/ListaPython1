"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 6 - Faça um Programa que peça a temperatura
em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 
Data: 08/09/21
"""
# Entrada de dados
print("------------------------------------------")
print("CONVERSOR DE FAHRENHEIT PARA GRAUS CELSIUS")
print("------------------------------------------")
print(" ")
valor_fahrenheit = float(input("Digite o valor, em Fahrenheit, que deseja converter para graus Celsius: "))
print(" ")

# Processamento de dados
valor_celsius = ((5 * (valor_fahrenheit - 32)) / 9)

# Saída de dados
print("----------------------")
print("Resultado da Conversão")
print("----------------------")
print(" ")
print(valor_fahrenheit, "grau(s) Fahrenheit equivale a", valor_celsius, "graus Celsius.")
