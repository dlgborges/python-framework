## **2 - Exercícios**

### **1. Classificação de Notas com Menção**

# Crie um programa que leia a nota de um aluno (0 a 10) e exiba a menção correspondente:

# - `"Excelente"` se nota >= 9
# - `"Bom"` se nota >= 7 e < 9
# - `"Regular"` se nota >= 5 e < 7
# - `"Insuficiente"` se nota < 5

### **2. Validação de Triângulo**

# Leia três lados de um triângulo. Verifique se eles formam um triângulo (cada lado é menor que a soma dos outros dois). Se sim, classifique como:

# - `"Equilátero"` (todos os lados iguais)
# - `"Isósceles"` (dois lados iguais)
# - `"Escaleno"` (todos diferentes)

# ### **3. Cálculo de IMC com Faixas**

# Leia peso (kg) e altura (m). Calcule o IMC e classifique conforme a tabela da OMS:

# - `"Abaixo do peso"` se IMC < 18.5
# - `"Peso normal"` se 18.5 ≤ IMC < 25
# - `"Sobrepeso"` se 25 ≤ IMC < 30
# - `"Obesidade"` se IMC ≥ 30

# Leia o salário bruto mensal e calcule o desconto do INSS (11% sobre o salário, limitado a R$ 1.500,00) e o IRRF conforme tabela:

# - Isento se salário bruto ≤ R$ 2.500,00
# - 7,5% sobre o que exceder R$ 2.500,00 até R$ 3.500,00
# - 15% sobre o que exceder R$ 3.500,00 até R$ 5.000,00
# - 27,5% sobre o que exceder R$ 5.000,00
    
#     Exiba o salário líquido após os descontos.

# salario_bruto_mensal = float(input('Qual o salário bruto mensal? '))
# desconto_inss, irrf, irrf_sete_meio, irrf_quinze, irrf_vinte_sete_meio = 0,0,0,0,0
# irrf_sete_meio = (salario_bruto_mensal - 2500) * 0.075
# irrf_quinze = 75 + ((salario_bruto_mensal - 3500) * 0.15)
# irrf_vinte_sete_meio = 75 + 225 + ((salario_bruto_mensal - 5000) * 0.275)


# if (salario_bruto_mensal * 0.11) <= 1500:
#     desconto_inss += salario_bruto_mensal * 0.11
# else:
#     desconto_inss += 1500

# if salario_bruto_mensal < 2500:
#     irrf = 0
# elif 2500 < salario_bruto_mensal <= 3500:
#     irrf += irrf_sete_meio
# elif 3500 < salario_bruto_mensal <= 5000:
#     irrf = irrf_quinze
# else:
#     irrf = irrf_vinte_sete_meio

# print('Desconto de INSS:', desconto_inss, '/ Imposto de Renda:', irrf, f'\nTotal de descontos: {desconto_inss + irrf}', f'\n\nSalário líquido: {salario_bruto_mensal - desconto_inss - irrf}')

### **10. Simulador de Caixa Eletrônico**

# Leia o valor a ser sacado (inteiro, múltiplo de 5, entre 10 e 1000).
# Calcule a menor quantidade possível de notas de 50, 20, 10 e 5.
# Exiba a quantidade de cada nota.
# Caso o valor não esteja dentro das regras, exiba uma mensagem de erro.

valor_saque = int(input('Qual valor deseja sacar, hoje (múltiplos de 5, entre 10 e 1000)? '))
mensagem_nao_saque = 'Não é possível sacar esse valor. Por favor, tente novamente.'
notas_cinquenta, notas_vinte = 0, 0
# valor_saque = 335
# multiplos_cinco = valor_saque // 5 = 60

if valor_saque > 50:
    notas_cinquenta += valor_saque // 50 # 6
    if valor_saque - (50 * notas_cinquenta) >= 20:
        notas_vinte = valor_saque - (50 * notas_cinquenta) // 20
        if valor_saque 


#determinar_notas:



if valor_saque == 5:
    print(mensagem_nao_saque)
elif valor_saque > 50:

