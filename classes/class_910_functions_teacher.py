def soma(x,y):
    return x + y


def subtrair(x,y):
    return x - y


def multiplicar(x,y):
    return x * y


def dividir(x,y):
    try:
        return x / y
            
    except ZeroDivisionError as erro:
        return erro



def operacoes():


    op =  input(':>>>')
    x = int(input('>>>'))
    y = int(input('>>>'))
    if op == '+':
       s  =  str(soma(x,y))
       print(s) 
       print(type(s))
    elif op == '-':
       s  =  str(subtrair(x,y))
       print(s) 
       print(type(s))


    elif op == '*':
       s  =  str(multiplicar(x,y))
       print(s) 
       print(type(s))   
    elif op == '/':
       s  =  str(dividir(x,y))
       print(s) 
       print(type(s))   
    else:
        print('Digite algo válido')           
operacoes()

# def cpf2():


#     cpf  =  input('CPF: ')
#     soma  = 0


#     for i in range(9):
#         soma += int(cpf[i]) * (10 - i)
    
#     nu1 = soma * 10
#     x1 = nu1 % 11
#     if x1 == 10:
#         x1 = 0
#     print(x1)



#     soma = 0
#     for i in range(10):
#         soma += int(cpf[i]) * (11 - i)


#     nu2 = soma * 10
#     x2 = nu2 % 11
#     if x2  == 10:
#         x2  = 0
#     print(x2)
   
   
    
#     if x1 ==  int(cpf[-2] and x2 ==  int(cpf[-1])):
#         print(True)
#     else:
#         print(False)    


# cpf2()




# tabuada 


# def tabuada(numero, inicio=1, fim=10):
#     for x in range(inicio,fim):
#         c  = x * numero
#         print( c)
     


# def mostrar():
#     tabuada(5,0,11)


# mostrar()    



#


# def contar_palavras(palavras_texto):
#     palavra = palavras_texto.split()
#     d =  {}
#     for i in palavra:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1    
        
#     print(d)


# contar_palavras('olá olá bom dia')    