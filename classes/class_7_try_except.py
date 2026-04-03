#1
# Trate o TypeError -  Qual expressão deve ser gerada para ele aparecer?

# nota_number = ''
# number = 3

# try:
#     print(nota_number + number)
# except TypeError as e:
#     print('TypeError: ', e)
# finally:
#     print('end of operation')

#2
# # Trate o ValueError -  Crie em python o erro
# nota_number = input('Type a name')

# try:
#     number = int(nota_number)
#     sum = number + 3
# except TypeError as e:
#     print('TypeError: ', e)
# except ValueError as e:
#     print('ValueError', e)
# finally:
#     print('end of operation')

#3
# Exercício: Dada uma lista, solicite ao usuário um índice e imprima o 
# elemento correspondente,
# lidando com exceções caso o índice fornecido esteja fora dos limites da lista.

# lista = ['Joao', 'Silvia', 'Bárbara', 'Sonia']

# try:
#     indice = int(input(f'Qual elemento da lista você quer saber o valor? Lista com {len(lista)} elementos. '))
#     print(lista[indice])
# except IndexError as e:
#     print('exception', e)
# finally:
#     print('Finally')

#4
# Peça ao usuário para inserir um número inteiro, tente convertê-lo 
# para um número real,
# lidando com exceções caso a entrada não seja um número ou não 
# seja possível converter para real.

# numero_inteiro = input('Informe um número inteiro: ')

# try:
#     inteiro = int(numero_inteiro)
#     numero_real = float(inteiro)
# except ValueError as e:
#     print('ValueError exceção', e)
# finally:
#     print('finally')

#5
# Exercício: Peça ao usuário para inserir dois números afaça a divisão do primeiro  
# pelo segundo, lidando com exceções caso o segundo número 
# seja zero.

print('Divisão de dois números\n')

try:
    primeiro = int(input('Insira o primeiro nro: \n'))
    segundo = int(input('Insira o segundo nro: \n'))
    print(f'Resultado do primeiro pelo segundo: {primeiro / segundo}\n ') 
except ZeroDivisionError as e:
    print('Divisão por zero não é permitida, Einstein!\n')
finally:
    print('Finally')
