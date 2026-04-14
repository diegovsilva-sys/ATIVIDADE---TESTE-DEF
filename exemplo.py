import os
import time
os.system("cls")

def calcular_idade(ano):
    idade = 2026 - ano
    print(f"idade: `{idade}")


print("= solicitando dados =")
ano_nascimento = int(input("Digite o ano de seu nascimento: "))

#   Chamando função para calcular idade.
calcular_idade(ano_nascimento)