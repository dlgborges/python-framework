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

class Rectangle:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura