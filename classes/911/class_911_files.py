import os

# def file_create(file_name):
#     input('Hit ENTER to continue...')

#     arquivo = open(file_name, 'w')
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.close()

# def file_modify(file_name, contents: str):
#     arquivo = open(file_name, 'a')
#     arquivo.write('Linha 3\n')
#     arquivo.close()

def file_remove(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)

def file_print_contents(file_name):
    if os.path.exists(file_name):
        arquivo = open(file_name, 'r')
        return arquivo.readlines()

# file_name = input('Qual o nome do arquivo a ser criado?')
# if os.path.exists(file_name):
#     os.remove(file_name)
#     create_file(file_name)
# else:
#     create_file(file_name)


arquivo_nome = 'cadastro.txt'
# remove file for a clean start
file_remove(arquivo_nome)

arquivo = open(arquivo_nome, 'w')
print('Informe nome e idade para cadastro:')

try:
    while True:
        nome = input('Nome: ')
        idade = input('Idade: ')
        arquivo.write(f'nome: {nome}, idade: {idade}\n')
        print('SAIR (CTRL+C) ou Informe nome e idade para cadastro:')
except KeyboardInterrupt:
    arquivo.close()
    print('\nCTRL+C identificado. Saindo do programa...') 

# print('Aqui está seu arquivo: \n', file_print_contents(arquivo_nome))

# 2. **Ler e exibir**
    
#     Escreva um programa que leia o arquivo `cadastro.txt` criado no exercício anterior e exiba na tela cada pessoa no formato `"Nome: [nome], Idade: [idade]"`

for line in file_print_contents(arquivo_nome):
    print(line)
    nome, idade = line.strip().split(',')

    #idade = line[1]

    print(f'Nome: {nome}, Idade: {idade}')
    
    # line_split = line.split(',')
    # print(line_split)
    # for i in line_split:
    #     print(i)
    #     clean_name = i.split(':')
    #     print(clean_name[-1])


# 3. **Contar linhas**  
#     Crie uma função `contar_linhas(nome_arquivo)` que retorna o número de linhas do arquivo. Teste com o arquivo `cadastro.txt`.


# 4. **Procurar palavra**
#     Peça ao usuário uma palavra e um nome de arquivo. Conte quantas vezes essa palavra aparece no arquivo (ignorando maiúsculas/minúsculas). Exiba o resultado.

    
# 5. **Copiar arquivo**
#     Peça ao usuário o nome de um arquivo de origem e um arquivo de destino. Copie o conteúdo do arquivo de origem para o destino, mantendo as linhas.
