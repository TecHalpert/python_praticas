import os
from CORES import cores

conversores = {"1":hex,
               "2":oct,
               "3":bin,
               }

def perguntas():
    while True:
        pergunta = input(f"Digite:\n"
                         f"{cores['verde']}1-Hexadecimal{cores['limitador']}\n"
                         f"{cores['amarelo']}2-Octadecimal{cores['limitador']}\n"
                         f"{cores['azul']}3-Binário{cores['limitador']}\n"
                         f"{cores['verde']}4-Sair{cores['limitador']}\n")
        if pergunta == "4":
            numero = 0
            return numero, pergunta
        elif pergunta not in ["1", "2", "3", "4"] :
            print("Valor inválido pae\nTenta de novo ae")
            input("Enter pra continuar...")
            os.system("cls")
            continue
        else:
            while(True):
               try:
                    numero = int(input(f"Digite um numero que deseja {cores['verde']}converter{cores['limitador']}: "))
                    os.system("cls")
                    pergunta = pergunta.strip()
                    return numero, pergunta
               except ValueError:
                    print("Valor inválido.\nTente Novamente.")
                    os.system("cls")

def conversor_ver_2(numero,pergunta):
    while pergunta != "4":
            if pergunta in conversores:
                resultado = conversores[pergunta](numero)[2:]
                print(f"O valor:{cores['branco']}{numero}{cores['limitador']} convertido ficou como:{cores['ciano']}{resultado}{cores['limitador']} ")
                input("Enter pra continuar...")
                os.system("cls")
                break
            else:
                print("Valor inválido amigo.")
                input("Enter pra continuar...")
                os.system("cls")
                numero,pergunta = perguntas()
                continue

def perguntaFim():
        while(True):
            continuidade = input("Vc deseja continuar a converter os números?\n1-Continuar\n2-Sair\n:")
            os.system("cls")
            continuidade = continuidade.strip()
            if continuidade == "1":
                    return continuidade
            elif continuidade == "2":
                print(f"Vc desejou encerrar.")
                return continuidade
            else:
                print("Vc inseriu um valor inválido!")
                continue

def conversor_app():
    controlador = ""
    while controlador != "2":
        numero, pergunta = perguntas()
        conversor_ver_2(numero, pergunta)
        if pergunta == "4":
            print("Vc encerrou o programa..")
            break
        else:
            controlador = perguntaFim()



conversor_app()












