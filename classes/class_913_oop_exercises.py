# ### **1. Classe Livro**
# Crie uma classe `Livro` com:

# - Atributos: `titulo`, `autor`, `ano`, `disponivel` (booleano, padrão True)
# - Métodos:
#     - `emprestar()`: se disponível, marca como False e exibe `"Livro emprestado"`; senão, exibe `"Indisponível"`
#     - `devolver()`: marca como True e exibe `"Livro devolvido"`
#     - `info()`: mostra todas as informações do livro
        
#         Crie dois livros, faça empréstimos e devoluções.

class Livro:
    def __init__(self, titulo: str, autor: str, ano: int, disponivel: bool = True):
        self.titulo: str = titulo
        self.autor: str = autor
        self.ano: int = ano
        self.disponivel: bool = disponivel
        print(f'Livro "{self.titulo}" cadastrado')

    def emprestar(self): # como informar o titulo do livro
        if self.disponivel:
            self.disponivel = False
            print(f'Livro "{self.titulo}" emprestado!')
        else:
            print(f'Livro "{self.titulo}" indisponível')
    
    def devolver(self): #como informar o titulo do livro
        self.disponivel = True
        print(f'Livro "{self.titulo}" devolvido!')

    def info(self):
        print(f'Título do livro: {self.titulo}, Autor: {self.autor}, Ano {self.ano}, {(print('Disponível para empréstimo') and self.disponivel) or (not self.disponivel and (print('Indisponível para empréstimo')))}')

livro_1 = Livro('Morte no Expresso do Oriente', 'Agatha Christie', 1934)
livro_2 = Livro('Bíblia Sagrada', 'Vários', 67)

livro_1.emprestar()
livro_1.devolver()
livro_1.info()

### **2. Classe Funcionário**
# Crie uma classe `Funcionario` com:

# - Atributos: `nome`, `cargo`, `salario_base`
# - Métodos:
#     - `aumentar_salario(percentual)`: aumenta o salário com base no percentual
#     - `calcular_bonus()`: retorna 10% do salário base
#     - `exibir_dados()`: exibe todas as informações
        
#         Crie um funcionário, aumente o salário e mostre os dados atualizados.

class Funcionario:
    def __init__(self, nome: str, cargo: str, salario_base: float):
        self.nome = nome
        self.cargo = cargo
        self.salario_base = salario_base

    def aumentar_salario(self, percentual: int):
        self.salario_base += (self.salario_base * (percentual/100))
    
    def calcular_bonus(self):
        return self.salario_base * 0.1
    
    def exibir_dados(self):
        print(f'Dados do funcionário: Nome: {self.nome}, Cargo: {self.cargo}, Salário: {self.salario_base}, Bônus: {self.calcular_bonus()}')

func = Funcionario('Dashiell', 'Eng. SW', 50000)
func.exibir_dados()

print(f'O bônus do funcionário {func.nome} é: {func.calcular_bonus()}')

func.aumentar_salario(15)

func.exibir_dados()

### **3./ Classe Calculadora (estática)**

# Crie uma classe `Calculadora` que **não precisa de atributos**. Apenas métodos de classe (use `@classmethod` ou métodos estáticos) para:

# - `somar(a, b)`
# - `subtrair(a, b)`
# - `multiplicar(a, b)`
# - `dividir(a, b)`
    
#     Teste os métodos sem criar objetos (chamando diretamente pela classe).

class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b
    
    @staticmethod
    def subtrair(a, b):
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
    @staticmethod
    def dividir(a, b):
        return a / b

operacao = 'soma'
print(f'A {operacao} dos números é igual a {Calculadora.somar(2, 2)}')

operacao = 'subtração'
print(f'A {operacao} dos números é igual a {Calculadora.somar(2, 2)}')

operacao = 'multiplicação'
print(f'A {operacao} dos números é igual a {Calculadora.somar(2, 2)}')

operacao = 'divisão'
print(f'A {operacao} dos números é igual a {Calculadora.somar(2, 2)}')