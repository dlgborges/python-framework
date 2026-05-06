# ### **1. Classe `Pessoa` com `__str__`**

# Crie uma classe `Pessoa` com atributos `nome`, `idade`, `email`. No construtor, receba e inicialize esses atributos. Implemente um método `__str__` que retorne uma string no formato `"Nome: [nome], Idade: [idade], Email: [email]"`. Crie duas pessoas e exiba-as.

# ---

# ### **2. Classe `Livro` com Métodos de Empréstimo**

# Crie uma classe `Livro` com atributos: `titulo`, `autor`, `disponivel` (booleano). No construtor, receba título e autor; `disponivel` deve começar como `True`. Métodos:

# - `emprestar()`: se disponível, muda para `False` e retorna `True`; senão, retorna `False`.
# - `devolver()`: muda para `True`.
# - `__str__()`: exibe informações + " (Disponível)" ou " (Emprestado)".
    
#     Teste criando um livro, emprestando e devolvendo.
    

# ---

# ### **3. Método de Classe para Criar Aluno Padrão**

# Classe `Aluno` com atributos `nome`, `matricula`, `curso`. Crie um método de classe `criar_aluno_padrao()` que retorna um aluno com nome `"Novo Aluno"`, matrícula gerada automaticamente (use um contador de classe) e curso `"Indefinido"`. Teste criando vários alunos com esse método.

# ---

# ### **4. Classe `Calculadora` com Métodos Estáticos**

# Crie uma classe `Calculadora` que **não precisa de construtor** (ou pode ter um vazio). Defina métodos estáticos:

# - `somar(a, b)`
# - `subtrair(a, b)`
# - `multiplicar(a, b)`
# - `dividir(a, b)` (trate divisão por zero com mensagem)
    
#     Teste chamando os métodos diretamente pela classe, sem instanciar objetos.
    

# ---

# ### **5. Classe `Carro` com Método Especial `__eq__`**

# Classe `Carro` com atributos `marca`, `modelo`, `ano`. No construtor, receba os três. Implemente o método `__eq__` para que dois carros sejam considerados iguais se tiverem a mesma marca, modelo e ano. Teste com dois carros iguais e dois diferentes.

# ---

# ### **6. Classe `ContaBancaria` com Métodos de Classe para Diferentes Tipos**

# Crie uma classe `ContaBancaria` com atributos `titular`, `saldo` (privado), `tipo` (ex: "corrente" ou "poupança"). No construtor, receba titular, saldo e tipo. Crie métodos de classe:

# - `criar_conta_corrente(titular)`: retorna uma conta corrente com saldo 0.
# - `criar_conta_poupanca(titular)`: retorna uma conta poupança com saldo 50.
    
#     Adicione métodos `depositar`, `sacar` e `__str__`. Teste.
    

# ---

# ### **7. Classe `Produto` com Método Estático de Validação**

# Classe `Produto` com atributos `nome`, `preco`, `quantidade`. No construtor, receba nome, preco, quantidade. O preço deve ser positivo (caso contrário, defina como 0). Crie um método estático `validar_preco(preco)` que retorna `True` se preço > 0. Use esse método dentro do construtor para validar. Teste criando produtos com preços válidos e inválidos.

# ---

# ### **8. Classe `Agenda` com Métodos de Instância e Construtor Personalizado**

# Crie uma classe `Contato` com atributos `nome`, `telefone`. Em seguida, crie a classe `Agenda` que possui um atributo `contatos` (lista). No construtor, você pode receber uma lista inicial (opcional). Métodos:

# - `adicionar_contato(contato)`
# - `listar_contatos()`: exibe todos
# - `buscar_contato(nome)`: retorna o contato ou `None`
    
#     Teste.
    

# ---

# ### **9. Classe `Funcionario` com Método Especial `__len__`**

# Classe `Funcionario` com atributos `nome`, `cargo`, `salario`. Crie um método `__len__` que retorna o tamanho do nome do funcionário (quantidade de caracteres). Teste: crie um funcionário e use `len(funcionario)`.

# ---

# ### **10. Classe `Data` com Métodos de Classe para Formatação**

# # Crie uma classe `Data` com atributos `dia`, `mes`, `ano`. No construtor, receba e valide a data. Implemente um método de classe `de_string(data_str)` que recebe uma string no formato `"dd/mm/aaaa"` e retorna um objeto `Data`. Implemente `__str__` para exibir `dd/mm/aaaa`. Teste criando datas de duas formas: via construtor direto e via método de classe.