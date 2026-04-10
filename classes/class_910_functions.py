# ### **1. Calculadora com Funções**

# Crie funções separadas para as quatro operações básicas (`somar`, `subtrair`, `multiplicar`, `dividir`). Em seguida, escreva um programa que leia dois números e a operação desejada (como string) e chame a função correspondente. A divisão deve tratar divisão por zero.

# ### **2. Validador de CPF (simplificado)**

# Crie uma função `validar_cpf(cpf)` que recebe uma string com 11 dígitos e retorna `True` se for válido (use o algoritmo básico de validação de CPF). Em seguida, teste a função com alguns CPFs.

# ### **3. Gerador de Tabuada**

# Escreva uma função `tabuada(numero, inicio=1, fim=10)` que exibe a tabuada do `numero` no intervalo `[inicio, fim]`. Se os argumentos `inicio` e `fim` não forem fornecidos, use 1 e 10.

# ### **4. Contador de Palavras**

# Crie uma função `contar_palavras(texto)` que retorna um dicionário com a contagem de cada palavra no texto (considere palavras separadas por espaços). O programa principal deve ler uma frase e exibir o resultado.

# ### **5. Ordenação Personalizada**

# Implemente uma função `ordenar_lista(lista, crescente=True)` que retorna uma nova lista ordenada. Se `crescente=True`, ordena em ordem crescente; caso contrário, decrescente. Não use `sorted()` ou `list.sort()` (implemente o algoritmo de ordenação de sua escolha, como bolha).

# ### **6. Jogo de Adivinhação**

# Crie uma função `jogar()` que sorteia um número entre 1 e 100 e dá dicas ("maior", "menor") até o usuário acertar. Use `random.randint()`. A função deve retornar o número de tentativas. No programa principal, chame a função e exiba quantas tentativas foram necessárias.

# ### **7. Conversor de Bases**

# Escreva uma função `converter_base(numero, base_origem, base_destino)` que converte um número entre bases 2, 8, 10 e 16. A entrada `numero` é uma string. A função retorna a string convertida. (Exemplo: `converter_base("1010", 2, 16)` → `"A"`). Use `int()` com base e depois formate.

# ### **8. Sistema de Caixa Eletrônico**

# Crie uma função `sacar(valor)` que retorna um dicionário com a quantidade de notas de 100, 50, 20, 10, 5 e 2 necessárias para o valor. O valor deve ser inteiro e positivo. Caso não seja possível (valor não múltiplo de 2), a função retorna `None`. No programa principal, chame a função e exiba o resultado.

# ### **9. Análise de Lista com Múltiplos Retornos**

# Escreva uma função `analisar_lista(lista)` que retorna quatro valores: o menor valor, o maior valor, a soma e a média. No programa principal, receba uma lista de números do usuário (terminada por -1) e exiba os resultados usando desempacotamento.

# ### **10. Função que Modifica Lista Global**

# Crie uma lista global `estoque = []`. Escreva funções:

# - `adicionar_produto(nome, quantidade)`: adiciona um dicionário `{"nome": nome, "quantidade": quantidade}` à lista global.
# - `remover_produto(nome)`: remove o produto com esse nome (se existir).
# - `listar_estoque()`: exibe todos os produtos.
    
#     Use a palavra-chave `global` para modificar a lista dentro das funções. O programa principal deve apresentar um menu interativo para o usuário.