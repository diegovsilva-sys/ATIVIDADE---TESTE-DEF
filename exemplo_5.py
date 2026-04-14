import os

os.system("cls")

def calcular_imc(peso, altura):
    return peso / (altura * altura)

def verificar_situacao(imc):
    if imc >=  40:
        claassificação = "Obesidade grau III"
        recomendação = "Busque assistência médica imediatamente"
    elif imc >= 35:
        claassificação = "Obesidade grau II"
        recomendação = "Consulte um médico parta avaliação e orientação"
    elif imc >= 30:
        claassificação = "Obesidade grau I"
        recomendação = "Procure orientação de um profissional de saúde"
    elif imc >= 25:
        claassificação = "  Sobrepeso"
        recomendação = "Considere uma dieta balanceada e atividade física"
    elif imc >= 18.5:
        claassificação = "Peso normal"
        recomendação = "Mantenha hábitos saudáveis"
    else:
        claassificação = "Abaixo do peso"
        recomendação = "Procure orientação"
    return claassificação, recomendação

print("= Solicitando dados =")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = calcular_imc(peso, altura)

classificacao, recomendacao = verificar_situacao(imc)

print("\n= Exibindo dados =")
print(f"IMC: {imc}")
print(f"Classificação: {classificacao}")