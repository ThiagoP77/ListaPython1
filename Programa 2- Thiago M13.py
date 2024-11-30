"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 2 - Faça um Programa que converta
metros para centímetros.
Data: 08/09/21
"""
# Entrada de dados
print("----------------------------------")
print("CONVERSOR DE METRO PARA CENTÍMETRO")
print("----------------------------------")
print(" ")
valor_metro = float(input("Informe o valor, em metros, que deseja converter para centímetros: "))
print(" ")

# Processamento de dados
valor_centimetros = (valor_metro*100)

# Saída de dados
print("----------------------")
print("Resultado da Conversão")
print("----------------------")
print(" ")
print(valor_metro, "metro(s) equivale a", valor_centimetros, "centímetros.")
