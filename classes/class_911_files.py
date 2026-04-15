import os

# def create_file(file_name):
#     input('Hit ENTER to continue...')

#     arquivo = open(file_name, 'w')
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.close()

# def modify_file(file_name, contents: str):
#     arquivo = open(file_name, 'a')
#     arquivo.write('Linha 3\n')
#     arquivo.close()


# file_name = input('Qual o nome do arquivo a ser criado?')
# if os.path.exists(file_name):
#     os.remove(file_name)
#     create_file(file_name)
# else:
#     create_file(file_name)

arquivo_nome = 'cadastro.txt'
arquivo = open(arquivo_nome, 'w')
print('Informe nome e idade para cadastro:')

while True:
    nome = input('Nome: ')
    idade = input('Idade: ')
    arquivo.write(f'nome: {nome}, idade: {idade}\n')
    print(arquivo_nome)
    print('SAIR (CTRL+C) ou Informe nome e idade para cadastro:')
