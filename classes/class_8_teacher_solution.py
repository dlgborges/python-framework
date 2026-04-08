import random

# Crie um programa que leia 
# a nota de um aluno (0 a 10) e exiba 
# a menção correspondente:

# nota  =  float(input('>>>  '))
# if nota  >= 9:
#     print('Excelente')
# elif nota >= 7 and nota <9:
#     print('Bom')
# elif nota >=5  and nota <9:
#     print('Regular')
# else:
#     print('insuficiente...')    



# # - `"Excelente"` se nota >= 9
# # - `"Bom"` se nota >= 7 e < 9
# # - `"Regular"` se nota >= 5 e < 7
# # - `"Insuficiente"` se nota < 5



# # # 2

# l1  =  float(input('lado 1 '))
# l2  =  float(input('lado 2 '))
# l3  =  float(input('lado 3 '))

# if l1 == l2 == l3 == l1:
#     print('equilatero')
# elif l1 != l2 != l3 != l1:
#     print('escaleno')
# else:
#     print('Isosceles')        

# 3

# peso =  float(input('Peso: '))
# altura  =  float(input('Altura: '))

# imc  = peso/(altura ** 2)
# print(imc)

# if imc < 18: print('abaixo do peso')
# elif imc>= 18 and imc <25:print('Peso normal')
# elif imc >=25 and imc <30:print('Sobrepeso')
# else:print('Obesidade') 

# try:
#     salario = float(input('Salário: '))

#     if salario >= 1501.00 and salario <= 2500.0:
#         if salario <= 1500.0:
#            print('Insento.. R$', salario )
#         sal =  salario
#         desconto_i = salario * 0.11
        
#         print('desconto INSS:', desconto_i )
#         print('Liquido ', sal - desconto_i )   
#     elif salario > 2500.0 and salario <= 3500.0:
#         sal =  salario
#         desconto =  salario * 0.075
#         inss =  salario * 0.11
#         print('desconto', desconto)
#         print('liquido', sal - desconto  + inss)  
#     elif salario > 3500.0 and salario <= 5000.0:
#         sal =  salario
#         desconto =  salario * 0.15
#         inss =  salario * 0.11
#         print('desconto', desconto)
#         print('liquido', sal - desconto  + inss )        
#     elif salario > 5000.0:
#         sal =  salario
#         desconto =  salario * 0.275
#         inss =  salario * 0.11
#         print('INSS', inss)
#         print('desconto', desconto)
#         print('liquido', sal - desconto + inss ) 
# except ValueError:
#        print('Digite algo válido')        


# 5 


# lista_opcoes  =  ['Pedra', 'Papel', 'Tesoura']
# aleatorio =  random.choice(lista_opcoes)
# escolha = input(f'Escolha: {lista_opcoes}')

# if aleatorio == escolha:
#     print('Empate')
# elif aleatorio == 'Pedra' and escolha == 'Tesoura':
#     print('Maquina ganhou!')
# elif aleatorio == 'Tesoura' and escolha == 'Papel':
#     print('Maquina ganhou!')
# elif aleatorio == 'Papel' and escolha == 'Pedra':
#     print('Maquina ganhou')  
# else:
#     print('Voc ganhou! ')     

# # elif aleatorio == 'Tesoura' and escolha == 'Pedra':
# #     print('Você ganhou!')
# # elif aleatorio == 'Papel' and escolha == 'Tesoura':
# #     print('Você ganhou!')
# # elif aleatorio == 'Pedra' and escolha == 'Papel':
# #     print('Você ganhou!')   

# print('escolha da maquina -- ', aleatorio)
# print('Minha escolha -- ', escolha)

# 7


# ano = int(input('Ano: '))
# sexo =  input('f ou m')
# deficiencia = input('sim ou não')

# idade  =  2026 - ano


    
# if sexo == 'f':
#     print('Não obrigatório')
# elif sexo == 'm' and  idade == 18 and deficiencia == 'não':
#     print('Aliste-se imediatamente') 
# elif sexo == 'm' and  idade >= 18 and deficiencia == 'sim':
#     print('Dispensado por saúde')
# elif sexo == 'm' and  idade < 18 and deficiencia == 'não':
#     mes = int(input('Mês: '))
#     print('Idade: ', idade)
#     print('Faltam : ',18 -  idade, 'anos... e', 8 - mes, 'meses' )
# elif idade > 18   and idade <=45:
#     print('Já passou do prazo')
# elif idade > 45:
#     print('Dispensado por idade')     
             
# 8

# idade =  int(input('Idade: '))
# plano =  input('b, s, p')

# if plano == 'b' and idade <= 60:
#     valor  =  (idade * 2) + 100
#     print('R$', valor)
# elif plano == 's' and idade <= 60:
#     valor  =  (idade * 3) + 150
#     print('R$', valor)    

# elif plano == 'p' and idade <= 60:
#     valor  =  (idade * 5) + 200
#     print('R$', valor)  

# else:
#     valor  =  (idade * 5) + 200
# #     print(valor) 
# #     acrescimo =  valor * 0.10
# #     print(acrescimo)
# #     print('R$', valor +acrescimo)   


# ano = int(input('Ano: '))
# dia = int(input('Dia: '))
# mes = int(input('mes: '))

# meses = [1,2,3,4,5,6,7,8,9,10,11,12]
# bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)
# print('Ano bissexto: ', ano and bissexto and 'é bissexto' or 'não é bissexto' )

# dias_meses = [
#     list(range(1,31)),  # 1
#     list(range(1,28)) if bissexto else list(range(1,29)),
#     list(range(1,31)), # 3
#     list(range(1,30)),  # 4
#     list(range(1,31)),  # 5
#     list(range(1,30)),  # 6
#     list(range(1,31)),  # 7
#     list(range(1,31)),  # 8
#     list(range(1,30)),  # 9
#     list(range(1,31)), # 10 
#     list(range(1,30)),  # 11
#     list(range(1,31))   # 12
# ]

# if mes in meses:
#     posicao = meses.index(mes)
#     if dia in dias_meses[posicao]:
#         print('Data válida')
#     else:
#         print('Dia inválido no mês...')
# else:
#     print('nao existe ')




# 10
valor  =  int(input('R$: '))

# valor entre 10 e 1000
# # 50, 20, 10, 5


l = [5,10,20,50]

if valor % 5 == 0:

    if valor == 10:
        quatidade_notas =  1
        print('R$', quatidade_notas)   
    elif valor  == 20 :
        quatidade_notas =  1
        print('R$', quatidade_notas)   
    elif valor == 50:
        quatidade_notas =  1
        print('R$', quatidade_notas)
    elif valor > 50:
         quantidade_notas_50 = valor // 50
         print(quantidade_notas_50,'notas de R$ 50')
         if quantidade_notas_50 * valor < valor:
             resto = quantidade_notas_50 -  valor
             print(resto)       
        
#          print(quantidade_notas_50)
#          quantidade_notas_20 = valor//20
#          print(quantidade_notas_20)
#          quantidade_notas_10 =  valor // 10
#          print(quantidade_notas_10)
#          quantidade_notas_5 =  valor // 5
#          print(quantidade_notas_5)

#          if quantidade_notas_50 * valor + quantidade_notas_20 * valor == valor:
#              print('Quantidade de notas 20 - ', quantidade_notas_20, '50')
#              print('Quantidade de notas 50 - ', quantidade_notas_50, '20')
#          elif quantidade_notas_50 * valor + quantidade_notas_20 * valor + quantidade_notas_10 * valor == valor:    
#              print('Quantidade de notas 20 - ', quantidade_notas_20)
#              print('Quantidade de notas 50 - ', quantidade_notas_50)
#          elif quantidade_notas_50 * valor + quantidade_notas_20 * valor + quantidade_notas_10 * valor + quantidade_notas_5 *5 == valor :   
#              print('Quantidade de notas 20 - ', quantidade_notas_20)
#              print('Quantidade de notas 50 - ', quantidade_notas_50)         
#              print('Quantidade de notas 20 - ', quantidade_notas_10)
#              print('Quantidade de notas 5 - ', quantidade_notas_5)
         
     


         
        
else:
    print('Erro ...')        



# # if valor % 10 and valor % 5 and valor % 50 and valor % 10:
# #     quantidade =  
# #     print()



    
