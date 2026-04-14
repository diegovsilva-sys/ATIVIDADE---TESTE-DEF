import os
from datetime import date

os.system("cls")


def calcular_idade(ano_nascimento):
    # Usa o ano atual.
    ano_atual = date.today().year()
    return ano_atual - ano_nascimento

print("= Solicitando dados =")
ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = calcular_idade(ano_nascimento)

print(("\n= Exibindo resultado"))
print(f"Idade: {idade}")