import random

class Jogador:
    def escolher(self):
        escolha = input('Escolha Pedra, Papel ou Tesoura: ')
        return escolha.lower()

class Maquina:
    def escolher(self):
        escolha = ['pedra', 'papel', 'tesoura']
        return random.choice(escolha)

class Jogo:
    def verificar_vitoria(self, jogador, maquina):
        if jogador == maquina:
            return 'EMPATE'
        elif jogador == 'pedra' and maquina == 'tesoura':
            return 'Jogador ganhou'
        elif jogador == 'papel' and maquina == 'pedra':
            return 'Jogador ganhou'
        elif jogador == 'tesoura' and maquina == 'papel':
            return 'Jogador ganhou'
        else:
            return 'Máquina venceu...'
    
    def jogar(self):
        jogador = Jogador()
        maquina = Maquina()

        escolha_jogador = jogador.escolher()
        escolha_maquina = maquina.escolher()

        print('Jogador escolheu', escolha_jogador)
        print('Máquina escolheu', escolha_maquina)

        resultado = self.verificar_vitoria(escolha_jogador, escolha_maquina)
        print('Resultado -> ', resultado)

jogo = Jogo()
jogo.jogar()
