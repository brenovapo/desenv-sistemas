#crie uma função que faça a media de 3 valores
#crie uma função que calcule o imposto anual do seu salario
#crie uma função que valide se a senha desafio esta correta

def calcular_media(valor1, valor2, valor3):
    media = (valor1 + valor2 + valor3) / 3
    print("Média: {media}")


def impostoanual(salario_mensal):
    salario_anual = salario_mensal * 12
    imposto = salario_anual * 0.15
    print("Imposto mensal", impostoanual )


def validar_senha(senha_digitada):
    senha_correta = 'desafio123'
    if senha_digitada == senha_correta:
        print("Senha correta!")
    else:
        print("Senha incorreta!")
    