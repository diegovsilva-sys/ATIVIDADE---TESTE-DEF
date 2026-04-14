import os

os.system("cls")

#Função com parametros.
def calcular_media(n1, n2):
    return (n1 + n2) / 2

#Exemplo de uso da função.
def verificar_situacao(media):
    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    return

print("= Solicitando dados =")
n1 = float(input("Digite o primeira nota: "))
n2 = float(input("Digite o segunda nota: "))

media = calcular_media(n1, n2)
situacao = verificar_situacao(media)

print("= Resultado =")
print(f"Media: {media}")
print(f"Resulatdo; {situacao}")