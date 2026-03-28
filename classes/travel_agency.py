import sys

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

destino = input('Qual o seu destino? ')
pessoas = int(input('Quantas pessoas irão viajar: '))

print(f'Obrigado! Vejo que você quer ir para {destino} com {pessoas} pessoas.\n\nVamos calcular o valor da viagem para você(s)')

sem_destino = destino not in viagens.keys()
valor_total = sem_destino + 0
sem_destino and print(f'Infelizmente, o destino não existe. Por favor, escolha um novo destino.') and sys.exit()

desconto = (destino == '') * valor_total

# Parte 2: Cálculo do Valor
# Calcule:
# Valor total da viagem (preço * pessoas)

destino_existe = viagens.get(destino)

valor_total = destino_existe and viagens.get(destino)['preco'] * pessoas
print(valor_total)
#print(f'O valor total da sua viagem ficaria em: {valor_total}, porém vejo que você pode ser elegível a alguns descontos:')

# Parte 3: Regras da Agência (SEM if, SEM loop)

# Aplique:
# Se pessoas > 3 → desconto de 10%
# Se valor total > 10000 → desconto extra de 5%
# Se não houver vagas suficientes → taxa de 500 (overbooking)
# Se destino não existir → valor vira 0

desconto_dez = pessoas > 3
valor_desconto_dez = desconto_dez and (valor_total * 0.1)
valor_total_desconto_dez = desconto_dez and (valor_total - valor_desconto_dez)

valor_total_desconto_dez and print(f'Como você está indo com mais de 3 pessoas, o valor total, com desconto, será de: {valor_total_desconto_dez}')

desconto_extra_cinco = valor_total > 10000
valor_desconto_cinco = desconto_extra_cinco and (valor_total * 0.05)
valor_total_desconto_extra_cinco = desconto_extra_cinco and (valor_total - valor_desconto_cinco)

(desconto_dez and desconto_extra_cinco and print(f'Como sua tarifa também está acima de 10000, você receberá um desconto extra de 5% e o total será de: {valor_total_desconto_dez - valor_desconto_cinco}')) and (desconto_extra_cinco and print(f'Como sua tarifa está acima de 10000, você receberá um desconto extra de 5% e o total será de: {valor_total_desconto_extra_cinco}'))

overbooking = viagens[destino]['vagas'] < pessoas
valor_total = valor_total - (valor_desconto_dez + valor_desconto_cinco + 500)
overbooking and print(f'Pelo fato de não termos mais o nro de vagas pedidas, há uma taxa de overbooking de 500R$. Sua tarifa será de: {valor_total}')


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
