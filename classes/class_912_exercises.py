# ### **1- Classe Pessoa**

# Crie uma classe `Pessoa` com os atributos `nome` e `idade`. Adicione um método `apresentar()` que exiba `"Olá, meu nome é [nome] e tenho [idade] anos."` Crie duas pessoas diferentes e chame o método.

class Person:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return self.nome, self.idade

    def teste_sem_self():
        pass

rodrigo = Person('Rodrigo', 32)
nome, idade = rodrigo.apresentar()
print(f'Nome da pessoa: {nome}, Idade da pessoa: {idade}')

catarina = Person('Catarina', 29)
nome, idade = catarina.apresentar()
print(f'Nome da pessoa: {nome}, Idade da pessoa: {idade}')

### **2.Classe Retângulo**
# Crie uma classe `Retangulo` com os atributos `largura` e `altura`. Adicione métodos:

# - `calcular_area()` – retorna a área
# - `calcular_perimetro()` – retorna o perímetro
    
#     Crie um retângulo com largura 5 e altura 3 e exiba sua área e perímetro.

class Rectangle:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return (self.largura + self.altura) * 2
    
rect = Rectangle(5,3)
print(f'A área do retângulo é igual a: {rect.calcular_area()} e seu perímetro é igual a: {rect.calcular_perimetro()}')

### **3.   Classe Conta Bancária**
# Crie uma classe `ContaBancaria` com:

# - Atributos: `titular`, `saldo` (inicial 0)
# - Métodos:
#     - `depositar(valor)`: acrescenta ao saldo
#     - `sacar(valor)`: se houver saldo suficiente, subtrai; senão, exibe `"Saldo insuficiente"`
#     - `exibir_saldo()`: mostra o saldo formatado

#         Crie uma conta, faça depósitos e saques e exiba o saldo.

class ContaBancaria:
    def __init__(self, titular:str, saldo:float=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor:float):
        self.saldo += valor

    def sacar(self, valor:float):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente')
    
    def exibir_saldo(self) -> str:
        return f'Seu saldo é de R$:{self.saldo}'

conta_001 = ContaBancaria('Dashiell')

conta_001.depositar(1000)
conta_001.sacar(500)
print(conta_001.exibir_saldo())

conta_001.sacar(1000)


### **4. Classe Produto**
# Crie uma classe `Produto` com:

# - Atributos: `nome`, `preco`, `quantidade_estoque`
# - Métodos:
#     - `total_estoque()`: retorna `preco * quantidade_estoque`
#     - `adicionar_estoque(quantidade)`: aumenta a quantidade
#     - `remover_estoque(quantidade)`: diminui, mas não permite ficar negativo
        
#         Crie um produto, altere o estoque e exiba o valor total.

class Produto:
    def __init__(self, nome: str, preco: float, estoque_quantidade: int=0):
        self.nome = nome
        self.preco = preco
        self.estoque_quantidade = estoque_quantidade

    def estoque_total(self) -> float:
        return self.preco * self.estoque_quantidade
    
    def estoque_adicionar(self, quantidade: int):
        self.estoque_quantidade += quantidade

    def estoque_remover(self, quantidade: int):
        if self.estoque_quantidade >= quantidade:
            self.estoque_quantidade -= quantidade
        else:
            print('Tentativa de remover o produto do estoque falhou: Não há quantidade suficiente do produto no estoque')

prod = Produto('Banana', 5.50, 300)
prod.estoque_adicionar(200)

print(f'O estoque total de {prod.nome} é de:R$', prod.estoque_total())

prod.estoque_remover(600)


### **5. Classe Aluno**
# Crie uma classe `Aluno` com:

# - Atributos: `nome`, `matricula`, `notas` (lista de floats)
# - Métodos:
#     - `adicionar_nota(nota)`: adiciona à lista
#     - `calcular_media()`: retorna a média das notas
#     - `situacao()`: retorna `"Aprovado"` se média >= 7, `"Recuperação"` se >= 5, `"Reprovado"` caso contrário
        
#         Crie um aluno, adicione 3 notas e exiba sua situação.

class Aluno:
    def __init__(self, nome: str, matricula: int, notas: list):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
    
    def nota_adicionar(self, nota: float):
        self.notas.append(nota)

    def media_calcular(self):
        return sum(self.notas)/len(self.notas)
    
    def situacao(self):
        media = self.media_calcular()

        if media >= 7:
            return 'Aprovado'
        elif media >= 5:
            return 'Recuperação'
        else:
            return 'Reprovado'

aluno_notas = [10, 3, 4.5, 9.4, 6.8, 7.3, 10]

stud = Aluno('Dashiell', 10001, aluno_notas)

print('O aluno está:', stud.situacao())