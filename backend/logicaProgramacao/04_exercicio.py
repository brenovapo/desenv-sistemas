salario = float (input("Digite seu salário "))

if salario > 5000:
    imposto_percentual = 0.08
else:
    imposto_percentual = 0.05

imposto_mensal = salario * imposto_percentual
imposto_anual = imposto_mensal * 12
salario_anual = salario * 12

print("Imposto mensal ", imposto_mensal )
print("Imposto anual ", imposto_anual )
print("Salário anual", salario_anual )













