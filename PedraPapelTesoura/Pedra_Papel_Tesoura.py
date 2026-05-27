import random
import os
from cores import cores

def limpador():
    return os.system("cls")
def pause():
    return input("Enter para continuar...")
jogadas = {'1': 'Pedra',
           '2': 'Papel',
            '3': 'Tesoura'}
def maquina():
    jogadaM =random.randint(1,3)
    return str(jogadaM)

def user(jogada):
    return jogada
def pedra_papel_tesoura(primeiro,segundo):
        if primeiro == segundo:
            return ("EMPATE")
        if primeiro == "1" and segundo == "3" or primeiro == "2" and segundo == "1" or primeiro == "3" and segundo == "2":
            return primeiro
        elif segundo == "1" and primeiro == "3" or segundo == "2" and primeiro == "1" or segundo == "3" and primeiro == "2":
            return segundo
        else:
            return ""
def decisaoF():
    pause()
    limpador()
    while(True):
        decisao = input("Deseja continuar a jogar?\n1-Sim\n2-Não")
        if (decisao == "1"):
            return "1"
        elif (decisao == "2"):
            return "2"
        else:
            continue
def jogo():
    pontuacaoPlayer = 0
    pontuacaoMaquina = 0
    def mostrar_resultado():
        return print(f"PLACAR:\n Você: {pontuacaoPlayer} X {pontuacaoMaquina} :Máquina")
    while True:
        jogadaPlayer = user(input("Digite:\n1-Pedra\n2-Papel\n3-Tesoura\n4-Sair\n:"))
        if jogadaPlayer == "4":
            if decisaoF() == "2":
                limpador()
                print(f"O Score final ficou em:\nVocê: {pontuacaoPlayer}\nMáquina: {pontuacaoMaquina}")
                input("Enter para encerrar...")
                limpador()
                break
            else:
                pause()
                limpador()
                continue
        else:
            jogadaMaquina = maquina()
            resultado = pedra_papel_tesoura(jogadaMaquina, jogadaPlayer)
            def mostrarPlacar():
                return print(f"Você: {jogadas[jogadaPlayer]} X {jogadas[jogadaMaquina]} :Máquina")

            limpador()
            if resultado == jogadaMaquina:
                pontuacaoMaquina += 1
                mostrarPlacar()
                print(
                    f"{cores['vermelhotxt']}Você perdeu!{cores['limitador']} {cores['azul']}{jogadas[jogadaMaquina]}{cores['limitador']} ganha de {cores['vermelho']}{jogadas[jogadaPlayer]}{cores['limitador']}")
                mostrar_resultado()
                pause()
                limpador()
            elif resultado == jogadaPlayer:
                pontuacaoPlayer += 1
                mostrarPlacar()
                print(
                    f"{cores['verde']}Você venceu!{cores['limitador']}Pois, {cores["azul"]}{jogadas[jogadaPlayer]}{cores['limitador']} ganha de {cores['vermelho']}{jogadas[jogadaMaquina]}{cores['limitador']}")
                mostrar_resultado()
                pause()
                limpador()
            elif resultado == "EMPATE":
                print(
                    f"Você: {cores['azul']}{jogadas[jogadaPlayer]}{cores['limitador']} X {cores['vermelho']}{jogadas[jogadaMaquina]}{cores['limitador']} :Máquina")
                print(f"{cores['amarelo']}EMPATOU!{cores['limitador']}")
                mostrar_resultado()
                pause()
                limpador()
            else:
                print(f"{cores['vermelho2']}Valor inválido.{cores['limitador']}")

jogo()



