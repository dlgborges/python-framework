from abc import ABC, abstractmethod

# ## **Exercícios extra com Streamlit…**

# **Classe Livro** – crie uma classe com atributos título, autor, ano. Adicione um método `__str__`. Crie uma subclasse `LivroDigital` que adiciona atributo `formato` e sobrescreva `__str__`.

class Livro:
    def __init__(self, titulo:str, autor:str, ano:int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f'Nome do livro: {self.titulo}, Autor: {self.autor}, Ano de publicação: {self.ano}'

class LivroDigital(Livro):
    def __init__(self, titulo:str, autor:str, ano:int, formato:str):
        super().__init__(titulo, autor, ano)
        self.formato = formato
    
    def __str__(self):
        return super().__str__() + f', Formato: {self.formato}'

crime_castigo = Livro('Crime e Castigo', 'dostoyevski', 1866)
print(crime_castigo.__str__())

sete_habitos = LivroDigital('Os sete hábitos das pessoas altamente eficazes', 'Stephen Covey', 1989, 'Digital')
print(sete_habitos.__str__())

# **Classe Abstrata Veiculo** – defina uma classe abstrata com método `mover`. Implemente `Carro` e `Bicicleta` com comportamentos diferentes. Teste o polimorfismo.

class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        super().__init__()

    def mover(self):
        return 'Acelerando o carro'
    
class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__()

    def mover(self):
        return 'Pedalando a bicicleta'

porsche = Carro()
print(porsche.mover())

caloi = Bicicleta()
print(caloi.mover())

# **Sobrecarga de operador** – crie uma classe `Vetor` com atributos x, y e implemente `__add__`, `__sub__`, `__mul__` (escalar).
class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self):
        return self.x + self.y

    def __sub__(self):
        return self.x - self.y
    
    def __mul__(self):
        return self.x * self.y
    
    def __div__(self):
        return self.x / self.y


# **Classe anônima** – use `type` para criar uma classe dinâmica com um método `saudacao`. Instancie-a.
