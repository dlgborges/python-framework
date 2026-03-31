viagens = {
    "Paris": {
        "preco": 5000,
        "vagas": 5
    },
    "Nova York": {
        "preco": 4000,
        "vagas": 3
    },
    "Tóquio": {
        "preco": 6000,
        "vagas": 2
    },
    "Teerã": {
        "preco": 1000,
        "vagas": 4
    }
}

# Parte 1: Escolha do Destino
# Peça ao usuário:
# Nome do destino
# Quantidade de pessoas

destino = input('Qual o seu destino? ')

sem_destino = destino not in viagens.keys()

pessoas = int(input('Quantas pessoas irão viajar: '))

print(f'Obrigado! Vejo que você quer ir para {destino} com {pessoas} pessoas.')

not sem_destino and print('Vamos calcular o valor da viagem para você(s)')

#desconto = (destino == '') * valor_total

# Parte 2: Cálculo do Valor
# Calcule:
# Valor total da viagem (preço * pessoas)

destino_existe = destino in viagens.keys()

valor_total = destino_existe and viagens.get(destino)['preco'] * pessoas
novo_valor_total = valor_total
#print(f'O valor total da sua viagem ficaria em: {valor_total}, porém vejo que você pode ser elegível a alguns descontos:')

# Parte 3: Regras da Agência (SEM if, SEM loop)

# Aplique:
# Se pessoas > 3 → desconto de 10%
desconto_dez = destino_existe and pessoas > 3
valor_desconto_dez = desconto_dez and (valor_total * 0.1)
novo_valor_total = valor_total - valor_desconto_dez
#valor_total_desconto_dez = desconto_dez and (valor_total - valor_desconto_dez)

#desconto_dez and print(f'O valor total, com desconto, para mais de 3 pessoas, será de: {novo_valor_total}')

# Se valor total > 10000 → desconto extra de 5%
desconto_extra_cinco = destino_existe and valor_total > 10000
valor_desconto_cinco = desconto_extra_cinco and (valor_total * 0.05)
novo_valor_total = novo_valor_total - valor_desconto_cinco

#(desconto_dez and desconto_extra_cinco and print(f'Como sua tarifa também está acima de 10000, você receberá um desconto extra de 5% e o total será de: {novo_valor_total}')) and (desconto_extra_cinco and print(f'Como sua tarifa está acima de 10000, você receberá um desconto extra de 5% e o total será de: {novo_valor_total}'))

# Se não houver vagas suficientes → taxa de 500 (overbooking)
overbooking = destino_existe and viagens[destino]['vagas'] < pessoas
novo_valor_total = overbooking and (novo_valor_total + 500)

#overbooking and print(f'Pelo fato de não termos mais o nro de vagas pedidas, há uma taxa de overbooking de 500R$. Sua tarifa será de: {novo_valor_total}')

(overbooking and desconto_extra_cinco and desconto_dez and print(f'O valor total, com desconto, para mais de 3 pessoas, tarifa acima de 10000 e que ultrapassa o nro de vagas disponíves, será de: {novo_valor_total}')) or (overbooking and desconto_dez and print(f'O valor total, com desconto, para mais de 3 pessoas, e que ultrapassa o nro de vagas disponíves, será de: {novo_valor_total}')) or (overbooking and desconto_extra_cinco and print(f'O valor total, com desconto de 5%, para tarifas acimas de 10000 e que ultrapassa o nro de vagas disponíves, será de: {novo_valor_total}')) or (desconto_dez and desconto_extra_cinco and print(f'O valor total, com desconto, para mais de 3 pessoas e tarifa acima de 10000, será de: {novo_valor_total}')) or (overbooking and print(f'O valor total da tarifa com nro de vagas maior do que as disponíves, será de: {novo_valor_total}'))


# Se destino não existir → valor vira 0
sem_destino and print(f'Infelizmente, o destino não está disponível. Por favor, repita a operação e escolha entre um dos destinos existentes: {list(viagens.keys())}') and sys.exit()
valor_total_sem_destino = 0
valor_total = valor_total_sem_destino


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
    "Tóquio": {
        "preco": 6000,
        "vagas": 2
    },
    "Teerã": {
        "preco": 1000,
        "vagas": 4
    }
}
