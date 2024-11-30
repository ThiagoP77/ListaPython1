"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa 1 - Faça um Programa que
peça as 4 notas bimestrais e mostre a média.
Data: 08/09/21
"""
# Entrada de dados
print("------------------------------")
print("CALCULADORA DE MÉDIA BIMESTRAL")
print("------------------------------")
print(" ")
print("-Informe os dados exigidos abaixo-")
print(" ")
nota1 = float(input("Informe sua primeira nota do bimestre: "))
nota2 = float(input("Informe sua segunda nota do bimestre: "))
nota3 = float(input("Informe sua terceira nota do bimestre: "))
nota4 = float(input("Informe sua quarta nota do bimestre: "))

# Processamento de dados
media_bimestral = ((nota1+nota2+nota3+nota4)/4)

# Saída de dados
print(" ")
print("---------")
print("Resultado")
print("---------")
print(" ")
print("Sua média bimestral é", media_bimestral)
