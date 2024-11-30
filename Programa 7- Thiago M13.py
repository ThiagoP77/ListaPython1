"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 7 - Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Farenheit.  
Data: 08/09/21
"""
# Entrada de dados
print("------------------------------------------")
print("CONVERSOR DE GRAUS CELSIUS PARA FAHRENHEIT")
print("------------------------------------------")
print(" ")
valor_celsius = float(input("Digite o valor, em graus Celsius, que deseja converter para Fahrenheit: "))
print(" ")

# Processamento de dados
valor_fahrenheit = (((valor_celsius * 9) / 5) + 32)

# Saída de dados
print("----------------------")
print("Resultado da Conversão")
print("----------------------")
print(" ")
print(valor_celsius, "grau(s) Celsius equivale a", valor_fahrenheit, "graus Fahrenheit.")
