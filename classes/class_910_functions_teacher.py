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