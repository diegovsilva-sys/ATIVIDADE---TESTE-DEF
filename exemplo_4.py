import os

os.system("cls")

def calcular_imc():
    print("--- Calculadora de IMC ---")
    try:
        # Solicita os dados ao usuário
        peso = float(input("Digite o seu peso em kg : "))
        altura = float(input("Digite a sua altura em metros : "))

        imc = peso / (altura ** 2)

        print(f"\nSeu IMC é: {imc:.2f}")

        if imc < 18.5:
            classificacao = "Abaixo do peso"
            recomendacao = "Consulte um nutricionista para orientação"
        elif 18.5 <= imc < 25:
            classificacao = "Peso normal"
            recomendacao = "Mantenha hábitos saudáveis!"
        elif 25 <= imc < 30:
            classificacao = "Sobrepeso"
            recomendacao = "Considere uma dieta balanceada e atividade física"
        elif 30 <= imc < 35:
            classificacao = "Obesidade grau 1"
            recomendacao = "Procure orientação de um profissional de saúde"
        elif 35 <= imc < 40:
            classificacao = "Obesidade grau 2"
            recomendacao = "Consulte um médico para avaliação e orientação"
        else:
            classificacao = "Obesidade grau 3"
            recomendacao = "Busque assistência médica imediatamente"

        # Exibe os resultados
        print(f"Classificação: {classificacao}")
        print(f"Recomendação: {recomendacao}")

    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos. Utilize ponto '.' em vez de vírgula ',' para casas decimais.")

# Executa o programa
if __name__ == "__main__":
    calcular_imc()