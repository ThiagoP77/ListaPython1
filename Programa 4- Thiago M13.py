"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 4 - Faça um Programa que calcule a área
de um quadrado, em seguida mostre o dobro desta área para o usuário.
Data: 08/09/21
"""
# Entrada de dados
print("---------------------------------------------------")
print("PROGRAMA PARA CALCULAR ÁREA DE QUADRADO E SEU DOBRO")
print("---------------------------------------------------")
print(" ")
lado_quadrado = float(input("Informe a medida do lado desse quadrado: "))
print(" ")

# Processamento de dados
area = lado_quadrado**2
dobro_area = area*2

# Saída de dados
print("-----------------------")
print("Resultados dos Cálculos")
print("-----------------------")
print(" ")
print("A área desse quadrado é igual a", area)
print("O dobro da área desse quadrado é igual a", dobro_area)
