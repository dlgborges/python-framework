# NÃO UTILIZE IF ELSE, LOOPS, FUNÇÕES, APENAS I/O, VARIÁVEIS, LISTAS, TUPLAS SINAIS LÓGICOS E ARITMÉTICOS

# 1. Verificação de maioridade e permissão
# Enunciado:
# Crie um programa que leia a idade do usuário e se ele possui autorização dos pais (responda True ou False).
# O usuário pode participar da atividade se tiver 18 anos ou mais ou tiver autorização dos pais.
# Use and / or para verificar e exiba "Pode participar" ou "Não pode participar".

# Exemplo:

# idade  = int(input('Idade: '))
# autorizacao = bool(input('Possui autorização?>>>  '))
# pode  =  idade >= 18 and autorizacao == True
# msg =  pode and "Pode participar" or "Não pode participar"
# print(msg)

# 2. Classificação de peso ideal
# Enunciado:
# Leia o peso (kg) e a altura (m) de uma pessoa. Calcule o IMC (peso / altura**2).
# Uma pessoa está com peso normal se o IMC estiver entre 18.5 e 24.9 (inclusive).
# Use operadores lógicos para verificar se o IMC está nessa faixa e exiba "Peso normal" ou "Fora da faixa".

print('Programa para calculcar o IMC')
peso = float(input('Qual o peso (em kg) do indivíduo? '))
altura = float(input('Qual a altura (em m) do indivíduo? '))
imc = peso / (altura**2)

peso_normal = imc > 18.5 and imc < 24.9
(peso_normal and print('Peso normal')) or (not peso_normal and print('Fora da faixa (tá gordinho(a))'))

# 3. Acesso ao sistema
# Enunciado:
# Leia o nome de usuário e a senha. O acesso é permitido apenas se o usuário for "admin" e a senha for "1234".
# Use and para verificar as duas condições e exiba "Acesso liberado" ou "Acesso negado".

usuário = input('Informe o nome do usuário: ')
senha = int(input('Informe a senha do usuário: '))
acesso_liberado = (usuário == 'admin' and senha == 1234)

(acesso_liberado and print('Acesso Liberado')) or (not acesso_liberado and print('Acesso Negado'))

# 4. Compra com desconto
# Enunciado:
# Leia o valor da compra e se o cliente é VIP (True ou False).
# O cliente ganha 10% de desconto se o valor for maior que R$ 100 ou ele for VIP.
# Exiba o valor final com desconto (se aplicável) ou o valor original.
valor_compra = float(input('Informe o valor da compra: '))
cliente_vip = input('Cliente VIP? S/N ').lower() == 's'
desconto_dez = (valor_compra > 100 or cliente_vip) and (valor_compra * 0.1)
valor_final = valor_compra - desconto_dez
print(f'O valor final da compra é de: {valor_final}')



# 5. Elegibilidade para doação de sangue
# Enunciado:
# Leia a idade e o peso.
# Para doar sangue, a pessoa deve ter entre 16 e 69 anos (inclusive) e pesar pelo menos 50 kg.
# Use and para verificar ambos os critérios e informe se a pessoa pode doar.
idade = int(input('Informe a idade do indivíduo: '))
peso = float(input('Informe o peso do indivíduo: '))
pode_doar = (idade > 16 and idade < 69) and (peso >= 50)

(pode_doar and print('Este indivíduo pode doar sangue')) or (not pode_doar and print('Este indivíduo NÃO pode doar sangue'))


# 6. Validação de horário de funcionamento
# Enunciado:
# Uma loja funciona de segunda a sexta, das 9h às 18h.
# Leia o dia da semana (1=segunda, 7=domingo) e a hora (0 a 23).
# Determine se a loja está aberta.
# Dica: use and para combinar dia útil com horário, e or se quiser tratar sábado/domingo como fechado.
print('Vamos verificar se a loja está aberta!')
dia_semana = int(input('Informe o dia da semana (1=segunda, 7=domingo): '))
hora = int(input('Informe a hora: '))

aberta = (dia_semana > 0 and dia_semana < 6) and (hora >=9 and hora <=23)

(aberta and print('A loja está aberta nesse horário')) or (not aberta and print('A loja NÃO está aberta nesse horário'))


# 7. Aprovação em duas disciplinas
# Enunciado:
# Leia as notas de Matemática e Português.
# O aluno é aprovado se ambas as notas forem maiores ou iguais a 6.
# Use and para verificar e exiba "Aprovado" ou "Reprovado".
nota_matematica = int(input('Informe a nota de Matemática: '))
nota_portugues = int(input('Informe a nota de Português: '))
aprovado = nota_matematica >= 6 and nota_portugues >= 6

(aprovado and print('Aprovado')) or (not aprovado and print('Reprovado'))

# 8. Identificação de ano bissexto
# Enunciado:
# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que também seja divisível por 400.
# Leia um ano e use and e or para determinar se ele é bissexto.
# Exiba "Ano bissexto" ou "Ano não bissexto".
ano = int(input('Informe o ano que deseja saber se é bissexto: '))
leap = (((ano % 4 == 0) and (not ano % 100 == 0)) and (ano % 400 == 0))

leap and print('Ano bissexto') or (not leap and print('Ano não bissexto'))



# 9. Faixa etária
# Enunciado:
# Leia a idade e classifique:

# "Criança" se idade < 12

# "Adolescente" se 12 ≤ idade ≤ 17

# "Adulto" se idade ≥ 18
# Use and e or para definir os intervalos e exiba a classificação.



# 10. Sistema de alerta de temperatura e umidade
# Enunciado:
# Leia a temperatura (°C) e a umidade (%).
# Dispare um alerta se temperatura > 35 ou umidade > 70.
# Caso contrário, exiba "Condições normais".
# Use or para combinar as condições.

