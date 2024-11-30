"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 5 - Faça um Programa que pergunte quanto você
ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
Data: 08/09/21
"""
# Entrada de dados
print("-----------------------------")
print("CALCULADORA DE SALÁRIO MENSAL")
print("-----------------------------")
print(" ")
print("-Informe os dados exigidos abaixo-")
print(" ")
ganho_por_hora = float(input("Digite o valor que você recebeu por hora de trabalho: "))
horas_mensais = float(input("Digite o número de horas de trabalho durante o mês: "))
print(" ")

# Processamento de dados
salario_mensal = (ganho_por_hora * horas_mensais)

# Saída de dados
print("--------------------")
print("Resultado do Cálculo")
print("--------------------")
print(" ")
print("Você recebeu um salário de R$", salario_mensal, "nesse referido mês.")
