import statistics

# sinais lógicos
# sinais aritméticos
# estruturas de dados
# funções build
# sinais aritmeticos
# sinais lógicos
# média 

# Lógica de programação:

# cadastrar o aluno
# cadastrar as notas do aluno > ok
# trazer média > nota
# trazer a média da sala 
# verificar qual a melhor média > media
# verifica qual a pior média > todas as media
# verificar de o aluno passou ou não >  medias

dados_escola = {}

nome_1 = input('Digite o nome: ')
nome_2 = input('Digite o nome: ')
nome_3 = input('Digite o nome: ')
nome_4 = input('Digite o nome: ')

dados_escola['alunos'] = []
dados_escola['alunos'].extend([nome_1, nome_2, nome_3,nome_4])

nota_aluno_1 = [float(input(f'Nota1 {nome_1}: ')), float(input(f'Nota2 {nome_1}: ')), float(input(f'Nota 3{nome_1}: '))]
nota_aluno_2 = [float(input(f'Nota1 {nome_2}: ')), float(input(f'Nota2 {nome_2}: ')), float(input(f'Nota3 {nome_2}: '))]
nota_aluno_3 = [float(input(f'Nota1 {nome_3}: ')), float(input(f'Nota2 {nome_3}: ')), float(input(f'Nota3 {nome_3}: '))]
nota_aluno_4 = [float(input(f'Nota1 {nome_4}: ')), float(input(f'Nota2 {nome_4}: ')), float(input(f'Nota3 {nome_4}: '))]

dados_escola['notas'] = []
dados_escola['notas'].extend([nota_aluno_1,nota_aluno_2,nota_aluno_3, nota_aluno_4])

media_aluno_1 = sum(dados_escola['notas'][0])/len(dados_escola['notas'][0])
media_aluno_2 = sum(dados_escola['notas'][1])/len(dados_escola['notas'][1])
media_aluno_3 = sum(dados_escola['notas'][2])/len(dados_escola['notas'][2])
media_aluno_4 = sum(dados_escola['notas'][3])/len(dados_escola['notas'][3])

n1 =  dados_escola['alunos'].index(nome_1)
n2 =  dados_escola['alunos'].index(nome_2)
n3 =  dados_escola['alunos'].index(nome_3)
n4 =  dados_escola['alunos'].index(nome_4)

print('-------------------------------------------')

print('Media aluno',dados_escola['alunos'][n1], media_aluno_1)
print('Media aluno',dados_escola['alunos'][n2], media_aluno_2)
print('Media aluno',dados_escola['alunos'][n3], media_aluno_3)
print('Media aluno',dados_escola['alunos'][n4], media_aluno_4)

dados_escola['media_sala'] = []
dados_escola['media_sala'].extend([media_aluno_1, media_aluno_2, media_aluno_3,media_aluno_4])

print('-------------------------------------------')

print('Medias da sala', dados_escola['media_sala'])

maior = max(dados_escola['media_sala'])
menor = min(dados_escola['media_sala'])

i1 = dados_escola['media_sala'].index(maior)
i2 =  dados_escola['media_sala'].index(menor)


print('-------------------------------------------')

print('Maior nota', maior, dados_escola['alunos'][i1])
print('Menor nota', menor, dados_escola['alunos'][i2])


print('-------------------------------------------')


print('Aprovados: ')

aprovado1 =  media_aluno_1 >= 7
aprovado2 =  media_aluno_2 >= 7
aprovado3 =  media_aluno_3 >= 7
aprovado4 =  media_aluno_4 >= 7


print('aluno situação', dados_escola['alunos'][0],'aprovado' ,aprovado1)
print('aluno situação', dados_escola['alunos'][1],'aprovado' ,aprovado2)
print('aluno situação', dados_escola['alunos'][2],'aprovado',aprovado3)
print('aluno situação', dados_escola['alunos'][3],'aprovado' ,aprovado4)



print(dados_escola)
