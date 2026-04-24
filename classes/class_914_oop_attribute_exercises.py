# ### **Exercício 1 – Livro**

# Crie uma classe `Livro` com atributos de instância: `titulo`, `autor`, `ano`, `emprestado` (booleano, padrão `False`). Métodos:

# - `emprestar()` – se disponível, muda `emprestado` para `True`.
# - `devolver()` – muda `emprestado` para `False`.
# - `__str__()` – retorna uma string com as informações.
    
#     Teste com dois livros.

# class Livro:
#     def __init__(self, titulo:str, autor:str, ano:int, emprestado:bool=False):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano = ano
#         self.emprestado = emprestado

#     def __str__(self):
#         return f'Título do livro: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Disponível: {('Sim' and self.emprestado == False) or (self.emprestado == True and 'Não')}'

#     def emprestar(self):
#         if self.emprestado == False:
#             self.emprestado = True
#             print(f'O livro "{self.titulo}" foi emprestado com sucesso.')
#         else:
#             print(f'O livro "{self.titulo}" já está emprestado.')
    
#     def devolver(self):
#         if self.emprestado == True:
#             self.emprestado = False
#             print(f'Livro "{self.titulo}" devolvido. Obrigado!')
#         else:
#             print('O livro só pode ser devolvido depois de ser emprestado')
    
# crime_castigo = Livro('Crime e Castigo', 'Dostoyevski', 1866)
# print(crime_castigo.__str__())
# crime_castigo.emprestar()
# crime_castigo.devolver()

# ---

# ### **Exercício 2 – Contador com Atributo de Classe**

# Crie uma classe `Contador` que tenha um atributo de classe `total_contadores` que conta quantas instâncias foram criadas. Cada vez que um novo objeto é criado, esse contador deve ser incrementado. Adicione um método `exibir_total()` que exibe o total de contadores criados.

# ---

# class Contador:
#     total_contadores = 0

#     def __init__(self):
#         Contador.total_contadores += 1
    
#     def exibir_total(self):
#         print(f'Temos um total de {self.total_contadores} Contadores')

# contador_1 = Contador()
# print(contador_1.total_contadores)
# contador_1.exibir_total()

# contador_2 = Contador()
# contador_2.exibir_total()

# ### **Exercício 3 – Produto com Desconto**

# Classe `Produto` com atributos privados `_nome`, `_preco`, `_quantidade`. Use propriedades (`@property`) para acessar esses atributos. Crie um método `aplicar_desconto(percentual)` que reduz o preço. O preço não pode ficar negativo. Teste criando produtos e aplicando descontos.

# ---

class Produto:
    def __init__(self, nome:str, preco:float, quantidade:int):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def preco(self) -> float:
        return self._preco
    
    @preco.setter
    def preco(self, novo_preco):
        self._preco = novo_preco

    @property
    def quantidade(self) -> int:
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, novo_quantidade):
        self._quantidade = novo_quantidade

    def aplicar_desconto(self, percentual):
        novo_preco = self._preco - (self._preco * (percentual/100))
        if novo_preco > 0:
            self._preco -= (self._preco * (percentual/100))
            print(f'{self._nome} agora custa {self._preco}')
        else:
            print('O preço do produto não pode ser negativo. Aplique um desconto menor')

macarrao = Produto('Macarrao', 5.5, 30)
macarrao.aplicar_desconto(30)
macarrao.aplicar_desconto(50)
macarrao.preco = 5.5
print(macarrao.preco)
macarrao.aplicar_desconto(30)
macarrao.aplicar_desconto(50)

# ### **Exercício 4 – Banco com Saldo Privado**

# Classe `ContaBancaria` com atributo privado `__saldo`. Métodos:

# - `depositar(valor)` – aumenta saldo.
# - `sacar(valor)` – reduz saldo se houver saldo suficiente; senão, exibe mensagem.
# - `exibir_saldo()` – retorna o saldo (use propriedade `saldo` apenas para leitura).
    
#     Crie uma conta, realize operações e exiba o saldo.
class ContaBancaria:
    def __init__(self, saldo:float):
        self.__saldo = saldo
        print(f'Nova conta bancária aberta com saldo de {self.exibir_saldo}')

    def depositar(self, valor:float):
        self.__saldo += valor

    def sacar(self, valor:float):
        if self.__saldo > valor:
            self.__saldo -= valor
        else:
            print('Não há saldo suficiente para o saque')
    
    @property
    def exibir_saldo(self):
        return self.__saldo

conta_1 = ContaBancaria(100)
conta_1.depositar(200)
conta_1.sacar(200)
conta_1.exibir_saldo
conta_1.sacar(200)
conta_1.exibir_saldo
    

# ---

# ### **Exercício 5 – Aluno com Notas**

# Classe `Aluno` com atributos: `nome`, `matricula` e uma lista privada `__notas`. Métodos:

# - `adicionar_nota(nota)` – adiciona à lista (valida de 0 a 10).
# - `calcular_media()` – retorna a média.
# - `situacao()` – retorna "Aprovado" se média >= 7, "Recuperação" se >= 5, "Reprovado" caso contrário.
    
#     Teste com um aluno e algumas notas.

# class Aluno:
#     def __init__(self, nome: str, matricula:int, notas:list[int]):
#         self.nome = nome
#         self.matricula = matricula
#         self.__notas = notas

#     def adicionar_nota(self, nota: int):
#         if 0 > nota > 10:
#             print('Entre com uma nota de 0 a 10')
#         else:
#             self.__notas.append(nota)
    
#     def calcular_media(self) -> float:
#         return sum(self.__notas) / len(self.__notas)
    
#     def situacao(self) -> str:
#         media = self.calcular_media()
#         match media:
#             case val if val >= 7:
#                 situacao = 'Aprovado'
#                 return situacao
#             case val if val >= 5:
#                 situacao = 'de Recuperação'
#                 return situacao
#             case _:
#                 situacao = 'Reprovado'
#                 return situacao
            

# joao = Aluno('Joao', 1, [3,5,7,9,2,10])
# joao.adicionar_nota(0)
# joao.adicionar_nota(11)
# joao.adicionar_nota(10)
# print(f'A média do aluno {joao.nome} é de {joao.calcular_media()} e ele está {joao.situacao()}')

# ---

# ### **Exercício 6 – Data (validação)**

# Crie uma classe `Data` com atributos `dia`, `mes`, `ano`. No `__init__`, valide se a data é válida (considere meses com 30/31 dias e ano bissexto para fevereiro). Use propriedades para garantir que alterações futuras também sejam validadas. Adicione um método `__str__` que retorna a data no formato `dd/mm/aaaa`.

# ---

# ### **Exercício 7 – Funcionário com Aumento**

# Classe `Funcionario` com atributos: `nome`, `cargo`, `salario_base` (privado). Métodos:

# - `aumentar_salario(percentual)` – aumenta o salário.
# - `calcular_bonus()` – retorna 10% do salário base.
# - Propriedade `salario` para leitura.
    
#     Teste criando um funcionário, aumente o salário e mostre o novo valor.
    

# ---

# ### **Exercício 8 – Carro com Velocidade (Encapsulamento)**

# Classe `Carro` com atributos `marca`, `modelo` e `__velocidade` (inicial 0). Métodos:

# - `acelerar(valor)` – aumenta velocidade até no máximo 200.
# - `frear(valor)` – reduz velocidade até no mínimo 0.
# - Propriedade `velocidade` para leitura.
    
#     Teste acelerando e freando.
    

# ---

# ### **Exercício 9 – Estatísticas (Atributos de Classe)**

# Classe `Estatistica` com atributos de classe `soma` e `contagem`. Métodos de classe:

# - `adicionar(valor)` – atualiza soma e contagem.
# - `calcular_media()` – retorna a média (ou 0 se nenhum valor adicionado).
    
#     Use `@classmethod` e não crie instâncias. Teste adicionando números e exibindo a média.
    

# ---

# ### **Exercício 10 – Agenda com Contatos (Composição)**

# Crie uma classe `Contato` com atributos `nome`, `telefone`, `email`. Crie uma classe `Agenda` que possui uma lista privada de contatos. Métodos:

# - `adicionar_contato(contato)` – adiciona à lista.
# - `listar_contatos()` – exibe todos os contatos.
# - `buscar_contato(nome)` – exibe os dados do primeiro contato com aquele nome.
    
#     Teste adicionando vários contatos e fazendo buscas.