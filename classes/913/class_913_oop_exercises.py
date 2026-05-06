# ### **1. Classe Livro**
# Crie uma classe `Livro` com:

# - Atributos: `titulo`, `autor`, `ano`, `disponivel` (booleano, padrão True)
# - Métodos:
#     - `emprestar()`: se disponível, marca como False e exibe `"Livro emprestado"`; senão, exibe `"Indisponível"`
#     - `devolver()`: marca como True e exibe `"Livro devolvido"`
#     - `info()`: mostra todas as informações do livro
        
#         Crie dois livros, faça empréstimos e devoluções.

# class Livro:
#     def __init__(self, titulo: str, autor: str, ano: int, disponivel: bool = True):
#         self.titulo: str = titulo
#         self.autor: str = autor
#         self.ano: int = ano
#         self.disponivel: bool = disponivel
#         print(f'Livro "{self.titulo}" cadastrado')

#     def emprestar(self): # como informar o titulo do livro
#         if self.disponivel:
#             self.disponivel = False
#             print(f'Livro "{self.titulo}" emprestado!')
#         else:
#             print(f'Livro "{self.titulo}" indisponível')
    
#     def devolver(self): #como informar o titulo do livro
#         self.disponivel = True
#         print(f'Livro "{self.titulo}" devolvido!')

#     def info(self):
#         print(f'Título do livro: {self.titulo}, Autor: {self.autor}, Ano {self.ano}, {(print('Disponível para empréstimo') and self.disponivel) or (not self.disponivel and (print('Indisponível para empréstimo')))}')

# livro_1 = Livro('Morte no Expresso do Oriente', 'Agatha Christie', 1934)
# livro_2 = Livro('Bíblia Sagrada', 'Vários', 67)

# livro_1.emprestar()
# livro_1.devolver()
# livro_1.info()

# ### **2. Classe Funcionário**
# # Crie uma classe `Funcionario` com:

# # - Atributos: `nome`, `cargo`, `salario_base`
# # - Métodos:
# #     - `aumentar_salario(percentual)`: aumenta o salário com base no percentual
# #     - `calcular_bonus()`: retorna 10% do salário base
# #     - `exibir_dados()`: exibe todas as informações
        
# #         Crie um funcionário, aumente o salário e mostre os dados atualizados.

# class Funcionario:
#     def __init__(self, nome: str, cargo: str, salario_base: float):
#         self.nome = nome
#         self.cargo = cargo
#         self.salario_base = salario_base

#     def aumentar_salario(self, percentual: int):
#         self.salario_base += (self.salario_base * (percentual/100))
    
#     def calcular_bonus(self):
#         return self.salario_base * 0.1
    
#     def exibir_dados(self):
#         print(f'Dados do funcionário: Nome: {self.nome}, Cargo: {self.cargo}, Salário: {self.salario_base}, Bônus: {self.calcular_bonus()}')

# func = Funcionario('Joaozinho', 'Pedreiro', 50000)
# func.exibir_dados()

# print(f'O bônus do funcionário {func.nome} é: {func.calcular_bonus()}')

# func.aumentar_salario(15)

# func.exibir_dados()

### **3./ Classe Calculadora (estática)**

# Crie uma classe `Calculadora` que **não precisa de atributos**. Apenas métodos de classe (use `@classmethod` ou métodos estáticos) para:

# - `somar(a, b)`
# - `subtrair(a, b)`
# - `multiplicar(a, b)`
# - `dividir(a, b)`
    
#     Teste os métodos sem criar objetos (chamando diretamente pela classe).

# class Calculadora:
#     @staticmethod
#     def somar(a, b):
#         return a + b
    
#     @staticmethod
#     def subtrair(a, b):
#         return a - b
    
#     @staticmethod
#     def multiplicar(a, b):
#         return a * b
    
#     @staticmethod
#     def dividir(a, b):
#         return a // b

# def operacao_texto(operacao_nome: str, operacao_calculo):
#     return f'A {operacao_nome} dos números é igual a {operacao_calculo}' 

# operacao, calculo = 'soma', Calculadora.somar(2, 2)
# print(operacao_texto(operacao, calculo))

# operacao, calculo = 'subtração', Calculadora.subtrair(2, 2)
# print(operacao_texto(operacao, calculo))

# operacao, calculo = 'multiplicação', Calculadora.multiplicar(2, 2)
# print(operacao_texto(operacao, calculo))

# operacao, calculo = 'divisão', Calculadora.dividir(2, 2)
# print(operacao_texto(operacao, calculo))

### **4. Classe Carro com Controle de Velocidade**
# Crie uma classe `Carro` com:

# - Atributos: `marca`, `modelo`, `velocidade` (inicial 0)
# - Métodos:
#     - `acelerar(valor)`: aumenta a velocidade (não pode ultrapassar 200 km/h)
#     - `frear(valor)`: diminui a velocidade (não pode ficar negativa)
#     - `velocidade_atual()`: exibe a velocidade
        
#         Crie um carro, acelere e freie até parar.

# class Carro:
#     def __init__(self, marca:str, modelo: str, velocidade:int=0):
#         self.marca = marca
#         self.modelo = modelo
#         self.velocidade = velocidade

#     def acelerar(self, valor:int):
#         print(f'Acelerando {valor} km/h', end='')
#         if self.velocidade + valor > 200:
#             print(' porém, a velocidade não pode ultrapassar 200 km/h')
#             self.velocidade_atual()
#         else:
#             self.velocidade += valor
#             self.velocidade_atual()
    
#     def frear(self, valor: int):
#         print(f'\nFreando {valor} km/h')
#         if self.velocidade - valor <= 0:
#             self.velocidade = 0
#             print('Carro parado')
#         else:
#             self.velocidade -= valor
#             self.velocidade_atual()

#     def velocidade_atual(self):
#         print(f'A velocidade do(a) {self.marca} {self.modelo} é: {self.velocidade} km/h')

# porsche = Carro('Porsche', '911', 100)

# porsche.velocidade_atual()

# porsche.acelerar(150)
# porsche.acelerar(100)

# porsche.frear(50)
# porsche.frear(100)

# porsche.frear(50)
# porsche.frear(100)

# ### **5. Classe Agenda**
# Crie uma classe `Agenda` que armazena contatos. Cada contato é um objeto da classe `Contato` (crie-a separada), com `nome`, `telefone` e `email`. A classe `Agenda` deve ter:

# - Atributo: `contatos` (lista)
# - Métodos:
#     - `adicionar_contato(contato)`: adiciona à lista
#     - `listar_contatos()`: exibe todos os contatos
#     - `buscar_contato(nome)`: exibe os dados do contato (se existir)
        
#         Crie alguns contatos, adicione-os à agenda e faça buscas.

class Contato:
    def __init__(self, nome: str, telefone: int, email:str):        
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Agenda:
    def __init__(self, contatos:list[Contato]):
        self.contatos = contatos
    
    def contato_adicionar(self, Contato):
        self.contatos.append(Contato)
        print('Contato adicionado à agenda!')
        self.contatos_listar()

    def contato_existe(self, nome) -> bool:
        for contato in self.contatos:
            if nome == contato.nome:
                return True
        return False
    
    def contato_remover(self, nome) -> bool:
        return False # quando o contato não foi removido

    def contato_listar(self, nome):
        pass

    def contatos_listar(self):
        print('Segue a lista de Contatos')
        for contato in self.contatos:
            print(f'Nome: {contato.nome},', f'Telefone: {contato.telefone},', f'email: {contato.email}')
    
    def contato_buscar(self, nome):
        if self.contato_existe(nome):
            for contato in self.contatos:
                if nome == contato.nome:
                    print('Contato encontrado!', f'Nome: {contato.nome},', f'Telefone: {contato.telefone},', f'email: {contato.email}')

joaozinho = Contato('Joaozinho', 985859898, 'joao@email.com')
mariazinha = Contato('Mariazinha', 958588989, 'maria@email.com')
contatos = [joaozinho, mariazinha]

agenda_geral = Agenda(contatos)
agenda_geral.contatos_listar()

pedrinho = Contato('Pedrinho', 933669988, 'pedro@email.com')

agenda_geral.contato_adicionar(pedrinho)
agenda_geral.contatos_listar()
agenda_geral.contato_buscar('Pedrinho')
agenda_geral.contatos_listar()