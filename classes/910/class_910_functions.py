from itertools import chain

# ### **1. Calculadora com Funções**
# Crie funções separadas para as quatro operações básicas (`somar`, `subtrair`, `multiplicar`, `dividir`). Em seguida, escreva um programa que leia dois números e a operação desejada (como string) e chame a função correspondente. A divisão deve tratar divisão por zero.
# def soma(x, y):
#     return x + y

# def subtracao(x, y):
#     return x - y

# def multiplicacao(x, y):
#     return x * y

# def divisao(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError as erro:
#         print('Divisão por 0 não existe, Einstein!') #return erro

# def saudacao():
#     operacao = input('''Escolha a operação que você deseja efetuar:
#                     1 - soma
#                     2 - subtracao
#                     3 - multiplicacao
#                     4 - divisao
#                     0 - SAIR
#                     ''')
#     numero_primeiro = int(input('Entre o primeiro número da operação: '))
#     numero_segundo= int(input('Entre o segundo número da operação: '))
#     return operacao, numero_primeiro, numero_segundo

# while True:
#     operacao, numero_primeiro, numero_segundo = saudacao()
#     match operacao:
#         case '1':
#             nome_operacao = 'soma'
#             print(f'O resultado da {nome_operacao} dos dois números é igual a:', soma(numero_primeiro, numero_segundo))
#         case '2':
#             nome_operacao = 'subtracao'
#             print(f'O resultado da {nome_operacao} dos dois números é igual a:', subtracao(numero_primeiro, numero_segundo))
#         case '3':
#             nome_operacao = 'multiplicacao'
#             print(f'O resultado da {nome_operacao} dos dois números é igual a:', multiplicacao(numero_primeiro, numero_segundo))
#         case '4':
#             nome_operacao = 'divisao'
#             print(f'O resultado da {nome_operacao} dos dois números é igual a:', divisao(numero_primeiro, numero_segundo))
#         case '0':
#             print('Saindo do programa.')
#             break


# ### **2. Validador de CPF (simplificado)**
# Crie uma função `validar_cpf(cpf)` que recebe uma string com 11 dígitos e retorna `True` se for válido (use o algoritmo básico de validação de CPF: https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/). Em seguida, teste a função com alguns CPFs.

# 1. Criar funcao que valida o CPF
 # Retorna valido ou invalido
 # CPF = string - vamos precisar parsear cada um dos números
# cpf = '52998224725'
# digito = cpf[-2:]


#print(digito, digito_primeiro, digito_segundo)
# multiplica_digito_primeiro = 0
# contador_cpf = 0

# def valida_qtd_digitos(cpf):
#     if len(cpf) > 11:
#         return cpf[0:11]

# def valida_digito_primeiro(cpf):
#     cpf = valida_qtd_digitos(cpf)
#     digito_primeiro = int(cpf[-2:-1])
#     multiplica_digito_primeiro = 0
#     contador_cpf = 0

#     for i in range(10, 1, -1):
#         #print(cpf[-len(cpf)])
#         multiplica_digito_primeiro += int(cpf[contador_cpf]) * i
#         contador_cpf += 1

#         # print(i)
#     # print(multiplica_digito_primeiro)

#     resto_multiplica_primeiro = multiplica_digito_primeiro * 10 % 11
#     # print(resto_multiplica_primeiro)

#     if resto_multiplica_primeiro == digito_primeiro:
#         return True

# def valida_digito_segundo(cpf):
#     digito_segundo = int(cpf[-1:])
#     multiplica_digito_segundo = 0
#     contador_cpf = 0

#     for i in range(11, 1, -1):
#         #print(cpf[-len(cpf)])
#         multiplica_digito_segundo += int(cpf[contador_cpf]) * i
#         contador_cpf += 1

#         # print(i)
#     # print(multiplica_digito_segundo)

#     resto_multiplica_segundo = multiplica_digito_segundo * 10 % 11
#     # print(resto_multiplica_segundo)

#     if resto_multiplica_segundo == digito_segundo:
#         return True



# def valida_cpf(valida_primeiro, valida_segundo, cpf):
#     i = 0
#     all_same = cpf[i] == cpf[i+1] == cpf[i+2] == cpf[i+3] == cpf[i+4] == cpf[i+5] == cpf[i+6] == cpf[i+7] == cpf[i+8] == cpf[i+9] == cpf[i+10]

#     if all_same:
#         return False
#     elif valida_primeiro or valida_segundo == False:
#         return False
#     elif valida_primeiro and valida_segundo == True:
#         return True
#     else:
#         return False

# # print('Primeiro dígito é válido?', valida_digito_primeiro(cpf))
# # print('Segundo dígito é válido?', valida_digito_segundo(cpf))

# # 2. Pedir o CPF ao usuário
# cpf = input('Informe o número (apenas os dígitos) de CPF para saber se é válido: ')

# # 3. Chamar a funcao que valida o CPF, usando o CPF como parametro de entrada
# cpf_valido = valida_cpf(valida_digito_primeiro(cpf) , valida_digito_segundo(cpf), cpf)

# ((cpf_valido) and print('CPF válido')) or (not (cpf_valido) and print('CPF Inválido'))


# # ### **3. Gerador de Tabuada**

# # Escreva uma função `tabuada(numero, inicio=1, fim=10)` que exibe a tabuada do `numero` no intervalo `[inicio, fim]`. Se os argumentos `inicio` e `fim` não forem fornecidos, use 1 e 10.

# def tabuada(numero, inicio=1, fim=10):
#     tabuada = []
#     start = 1

#     for i in range(inicio,fim):
#         tabuada.append(f'{numero} x {i} = {numero * i}')
#     print(tabuada)

# while True:
#     numero = int(input('Informe um número inteiro positivo para calcularmos sua tabuada: '))
#     inicio, fim = int(input('Informe o intervalo da tabuada a ser calculado (ex. 1, 10 = 1 ao 10| 2,4 = 2 ao 4)')).split(",")
#     tabuada(numero, inicio, fim)
#     break


# ### **4. Contador de Palavras**
# Crie uma função `contar_palavras(texto)` que retorna um dicionário com a contagem de cada palavra no texto (considere palavras separadas por espaços). O programa principal deve ler uma frase e exibir o resultado.
# def conta_palavras(text):
#     split_text = text.split()
#     dict_text = {}
#     # count = 0
    
#     for i in split_text:
#         if i in dict_text:
#             dict_text[i] += 1
#         else:
#             dict_text[i] = 1
    
#     return dict_text

# print(conta_palavras('teste de conta palavras no teste de contagem de palavras grandes e pequenas'))

# ### **5. Ordenação Personalizada**
# Implemente uma função `ordenar_lista(lista, crescente=True)` que retorna uma nova lista ordenada. Se `crescente=True`, ordena em ordem crescente; caso contrário, decrescente. Não use `sorted()` ou `list.sort()` (implemente o algoritmo de ordenação de sua escolha, como bolha).
lista = [12,2,8,4,5,6,7,3,1,14,15,8,2,1] #[15, 8, 10, 1]

def criar_set(lista):
    lista_set = []
    for i in lista:
        if len(lista_set) < 1 :
            lista_set.append(i)
        else:
            if i in lista_set:
                continue
            else:
                lista_set.append(i)
    
    return lista_set
        

def ordenar_lista(lista, crescente=True):
    print('Vamos ordenar essa lista!')
    lista_ordenada = []

    # pega o primeiro e compara com o próximo e assim por diante, até o último
    # Caso crescente - solução 1:
     # Se o nro sendo comparado for maior do que o próximo, comparar com o próximo até que não seja maior colocar o primeiro na posição do segundo (vai deslocar o segundo para a direita)     
      # Se não, coloca o segundo na posição do primeiro index()

    # Caso crescente - solução 2:
     # Achar o MAIOR nro e colocá-lo na última posição da lista (lista[-1] = MAIOR) até esgotar a lista
      # A lista vai diminuindo (o último elemento não precisa ser lido, já sabemos que é o MAIOR). O próximo MAIOR entra na posição lista[-2] e assim por diante.


    for i in lista:
        print('i', i)
        for x in range(len(lista)):
            print('x', x)
            if len(lista_ordenada) < 1: #i < lista[x] and
                lista_ordenada.append(i)
                print(lista_ordenada)
                break
            else:
                if crescente == True: #and i not in lista_ordenada:
                    if i < lista[x]:
                        print('list[x]', lista[x])
                        lista_ordenada.insert(x, i)
                        print(lista_ordenada)
                        break
                    else:
                        lista_ordenada.insert(lista.index(i)+1, lista[x])
                else:
                    if i > lista[x]: #and i not in lista_ordenada:
                        print('list[x]', lista[x])
                        lista_ordenada.insert(x, i)
                        print(lista_ordenada)
                        break
                    else:
                        continue
    
    return lista_ordenada

#print(criar_set(lista))

print(ordenar_lista(criar_set(lista)))



# ### **6. Jogo de Adivinhação**

# Crie uma função `jogar()` que sorteia um número entre 1 e 100 e dá dicas ("maior", "menor") até o usuário acertar. Use `random.randint()`. A função deve retornar o número de tentativas. No programa principal, chame a função e exiba quantas tentativas foram necessárias.

# ### **7. Conversor de Bases**

# Escreva uma função `converter_base(numero, base_origem, base_destino)` que converte um número entre bases 2, 8, 10 e 16. A entrada `numero` é uma string. A função retorna a string convertida. (Exemplo: `converter_base("1010", 2, 16)` → `"A"`). Use `int()` com base e depois formate.

# ### **8. Sistema de Caixa Eletrônico**

# Crie uma função `sacar(valor)` que retorna um dicionário com a quantidade de notas de 100, 50, 20, 10, 5 e 2 necessárias para o valor. O valor deve ser inteiro e positivo. Caso não seja possível (valor não múltiplo de 2), a função retorna `None`. No programa principal, chame a função e exiba o resultado.

# ### **9. Análise de Lista com Múltiplos Retornos**

# Escreva uma função `analisar_lista(lista)` que retorna quatro valores: o menor valor, o maior valor, a soma e a média. No programa principal, receba uma lista de números do usuário (terminada por -1) e exiba os resultados usando desempacotamento.

# ### **10. Função que Modifica Lista Global**

# Crie uma lista global `estoque = []`. Escreva funções:

# - `adicionar_produto(nome, quantidade)`: adiciona um dicionário `{"nome": nome, "quantidade": quantidade}` à lista global.
# - `remover_produto(nome)`: remove o produto com esse nome (se existir).
# - `listar_estoque()`: exibe todos os produtos.
    
#     Use a palavra-chave `global` para modificar a lista dentro das funções. O programa principal deve apresentar um menu interativo para o usuário.