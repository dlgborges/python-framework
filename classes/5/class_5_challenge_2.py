#     Contexto:
# Uma indústria monitora temperatura (T), umidade (U) e presença de gás inflamável (G, 0 ou 1).
# O nível de risco é dado por:

# Crítico: (T > 40 ou U > 80) e G == 1

# Alto: (T > 40 ou U > 80) e G == 0

# Médio: (T entre 25 e 40) e (U entre 50 e 80)

# Baixo: qualquer outra situação

# Tarefa:
# Receba T (float), U (float), G (0 ou 1).
# Classifique o risco em "Crítico", "Alto", "Médio" ou "Baixo" sem usar if/elif.
# Use apenas dicionários com chaves booleanas e operadores lógico

# UTILIZE APENAS SINAIS LÓGICOS -  VARIAVEIS  -  LISTAS  -  I/O -  NÃO UTILIZE CONDICIONAIS OU LOOPS

riscos = {
    'Crítico':{
        'Temperatura Mínima': 40,
        'Umidade Mínima': 80,
        'Gás': True
    },
    'Alto':{
        'Temperatura Mínima': 40,
        'Umidade Mínima': 80,
        'Gás': False
    },
    'Médio':{
        'Temperatura Mínima': 25,
        'Temperatura Máxima': 40,
        'Umidade Mínima': 50,
        'Umidade Máxima': 80,
        'Gás': False
    },
    'Baixo':{

    }
}

temperatura = float(input('Informe a temperatura (°C): '))
umidade = float(input('Informe a umidade do ar (%): '))
gas = int(input('Existe a presença de gás? (0 - Não, 1 - Sim) '))

critico = (temperatura > 40 or umidade > 80) and gas
alto = (temperatura > 40 or umidade > 80) and not gas
medio = (25 <= temperatura <= 40 and 50 <= umidade <= 80)
baixo = not critico and not alto and not medio

((critico and print('Crítico')) or (not critico and alto and print('Alto')) or (not critico and not alto and medio and print('Médio')) or (not critico and not alto and not medio and print('Baixo')))