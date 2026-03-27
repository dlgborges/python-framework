viagens = {
    "Paris": {
        "preco": 5000,
        "vagas": 5
    },
    "Nova York": {
        "preco": 4000,
        "vagas": 3
    },
    "Tokyo": {
        "preco": 6000,
        "vagas": 2
    }
}

# Parte 1: Escolha do Destino
# Peça ao usuário:
# Nome do destino
# Quantidade de pessoas

destino = input('Qual o seu destino?')
pessoas = int(input('Quantas pessoas irão viajar'))

# Parte 2: Cálculo do Valor
# Calcule:
# Valor total da viagem (preço * pessoas)

valor_total = viagens[destino] * pessoas

# Parte 3: Regras da Agência (SEM if, SEM loop)

# Aplique:
# Se pessoas > 3 → desconto de 10%
# Se valor total > 10000 → desconto extra de 5%
# Se não houver vagas suficientes → taxa de 500 (overbooking)
# Se destino não existir → valor vira 0

desconto_dez = pessoas > 3
desconto_extra_cinco = valor_total > 10000
overbooking = viagens[destino]['vagas']


# ---------------------------------------------------------
viagens = {
    "Paris": {
        "preco": 5000,
        "vagas": 5
    },
    "Nova York": {
        "preco": 4000,
        "vagas": 3
    },
    "Tokyo": {
        "preco": 6000,
        "vagas": 2
    }
}
