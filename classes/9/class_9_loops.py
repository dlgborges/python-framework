from itertools import chain
import getpass
import datetime
import random

# ## **2  - Exercícios**

# ### **1. Tabuada Personalizada**
# Peça ao usuário um número inteiro positivo. Use `for` para exibir a tabuada desse número de 1 a 10.

# **Exemplo:**
# `Digite um número: 7` → exibe 7 x 1 = 7, 7 x 2 = 14, ..., 7 x 10 = 70.

numero = int(input('Informe um número inteiro positivo para calcularmos sua tabuada (1 ao 10): '))
tabuada = []
start = 1

for i in range(1,11):
    tabuada.append(f'{numero} x {i} = {numero * i}')
print(tabuada)

l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

l = [x for x in chain(l1,l2,l3)]
print(l)
# ---

# ### **2. Contagem Regressiva com Pausa**
# Peça um número inteiro positivo. Use `while` para fazer uma contagem regressiva até 0, exibindo cada número. Após o término, exiba `"Fogo!"`.
numero = int(input('Informe um número inteiro positivo para fazermos contagem regressiva: '))

while numero >= 0:
    print(numero)
    numero -= 1
print('Fogo')

try:
    while numero >= 0:
        print(numero)
        numero -= 1
finally:
    print('Fogo')

# ---

# ### **3. Média de Notas com `while`**
# Peça notas até que o usuário digite `-1`. Calcule e exiba a média das notas válidas (0 a 10). Ignore entradas inválidas e use `continue` quando necessário.
media = []
nota = 0

while nota != -1:
    nota = input('Informe a nota a ser inserida na lista ou -1 para sair: ')
    if (nota == -1 or nota == '-1') and len(media) > 0:
        media_notas = sum(media) / len(media)
        print('Saindo do programa')
        print(f'A média das notas é: {media_notas}')
        break
    elif (nota == -1 or nota == '-1') and len(media) == 0:
        print('Saindo do programa. Sem notas para calcular a média.')
        break
    elif not nota.isnumeric() or int(nota) <= -2 or int(nota) > 10:
        print('O número é negativo, não é um número ou é maior do que 10.')
        continue
    else:
        nota = int(nota)
        media.append(nota)

media_notas = sum(media) / len(media)
print('A média das notas é: {media_notas}')


# ---
# ### **4. Validação de Senha com Limite de Tentativas**
# Defina uma senha fixa (ex: `"python123"`). Dê ao usuário 3 tentativas usando `while`. Se acertar, exiba `"Acesso liberado"` e encerre. Se errar todas, exiba `"Conta bloqueada"`.
senha = 'python123'
senha_usuario = getpass.getpass('Informe a senha: ')
tentativas = 3

while senha_usuario != senha:
    tentativas -= 1
    if tentativas == 0:
        print('Conta bloqueada')
        break
    else:
        print(f'Senha incorreta, você tem mais {tentativas} tentativas antes de sua conta ser bloqueada.')
        senha_usuario = getpass.getpass('Informe a senha: ')
else:
    print('Acesso Liberado')


# ---
# ### **5. Números Primos**
# Peça um número inteiro positivo e determine se ele é primo. Use `for` com `range` e `break` para otimizar.

#nros primos:  

print('Vamos descobrir se um número é primo?')

for i in range(100):
    primo = input('Por favor, informe o número ou SAIR para interromper: ')
    if primo.isnumeric():
        primo_int = int(primo)
    
    if not primo.isnumeric() and primo.lower() == 'sair':
        print('Encerrando o programa.')
        break
    elif primo_int == 2 or primo_int == 3 or (primo_int % 2 != 0 and primo_int % 3 != 0):
        print(f'O número {primo_int} é Primo')
    # elif primo % 2 == 0:
    #     print('Não é primo')
    else:
        print(f'O número {primo_int} não é Primo')

# ---
# ### **6. Sequência de Fibonacci**
# Gere os primeiros N termos da sequência de Fibonacci, onde N é informado pelo usuário. Use `for` ou `while` para iterar.
termos = int(input('Quantos termos (nro inteiro, positivo) da sequência de Fibonacci iremos calcular? '))
termos_lista = [0,1]

for i in range(0, termos + 1):
    proximo_numero = termos_lista[i] + termos_lista[i+1]
    termos_lista.append(proximo_numero)
    ##print(termos_lista)

print(termos_lista)


# ---
# ### **7. Soma de Dígitos**
# Peça um número inteiro positivo e calcule a soma de seus dígitos. Use `while` para extrair os dígitos um a um.
numero = int(input('Informe um nro inteiro, positivo, para o cálculo: '))
soma = 0

if numero > 9:
    numero_split = str(numero)
    for i in numero_split:
        soma += int(i)
    print(soma)
else:
    print(f'Número menor do que 10. A soma dos dígitos é igual ao próprio número:', numero)


# ---
# ### **8 Menu Interativo**
# Crie um menu que permaneça ativo até que o usuário escolha a opção `"Sair"`. As opções podem ser:

# - `1` – Exibir mensagem "Olá!"
# - `2` – Exibir a data/hora atual (use `import datetime`)
# - `3` – Sair

# Use `while True` e `break` para sair.

opcao = input('''
          Bem vindo. Escolha sua opção:
          1 - Para receber saudação
          2 - Para exibir data/hora atual
          3 - Para SAIR do programa
        
          Opção: ''')

print('\n\t')

while True:
    match opcao:
        case '3':
            print('Saindo do programa.')
            break
        case '2':
            print(f'\tDia e a hora atuais: {datetime.datetime.now().strftime('%c')}')
        case '1':
            print('\tSaudações!')
    
    opcao = input('''
          Escolha sua opção:
          1 - Para receber saudação
          2 - Para exibir data/hora atual
          3 - Para SAIR do programa
        
          Opção: ''')
    
    print('\n\t')

# ---
# ### **9 Simulador de Lançamento de Dados**
# Simule 100 lançamentos de um dado de 6 faces. Conte quantas vezes cada face foi sorteada e exiba o resultado. Use `for` e `random.randint(1,6)`. (Importe `random`.)
print('Lançamento de dados com random.randint. Cálculo de quantas vezes cada número apareceu:')

lancamentos = []

for i in range(100):
    lancamentos.append(random.randint(1,6))

print(f'''O dado foi lançado {len(lancamentos)} vezes.
      O número 1 apareceu {lancamentos.count(1)} vezes
      O número 2 apareceu {lancamentos.count(2)} vezes
      O número 3 apareceu {lancamentos.count(3)} vezes
      O número 4 apareceu {lancamentos.count(4)} vezes
      O número 5 apareceu {lancamentos.count(5)} vezes
      O número 6 apareceu {lancamentos.count(6)} vezes
      
      Um possível próximo passo seria investigar se o "dado" está viciado''')
