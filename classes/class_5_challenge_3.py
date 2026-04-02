# Contexto
# Uma loja oferece um cupom especial. O cliente ganha o cupom se atender a pelo menos uma das seguintes condições:

#  Se for VIP (responde "sim" ou "não")
# Valor da compra acima de R$ 200
# Primeira compra no mês (responder "sim" ou "nao")

# Além disso, o cupom  pode ser aplicado se o cliente tiver  no histórico (número inteiro).Tarefa
# Receba:
# vip (string "sim" ou "nao")
# valor (float)
# primeira_compra (string "sim" ou "nao")
# itens_defeito (int)

# Determine se o cliente  ("Cupom liberado") ou  ("Sem cupom"),  (SEM IF , SEM LOOP, SEM FUNÇÃO)

vip = input('Cliente VIP? Não, Sim: '))
valor = float(input('Valor da Compra: '))
primeira_compra_mes = input('Primeira compra no mês? ')
itens_defeito = input('Itens tem defeito? 0 - Não, 1 - Sim: ')

cupom = ((vip.lower() == 'sim' or (valor > 200) or primeira_compra_mes.lower() == 'nao') and print('Cupom liberado')) or print('Sem cupom')