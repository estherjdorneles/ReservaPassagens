import random
import sys

"""
Sistema de reserva de passagem par a Viação União Santa Cruz

objetivos:

1 - Mostrar o mapa de cada ônibus em quatro possíveis viagens = 4 mapas de assentos.
    Ônibus amanhã: 6h (32 disponíveis, 14 ocupados), 10h (39 disponíveis, 7 ocupados)
    Ônibus tarde: 16h (32 disponíveis, 14 ocupados), 20h (39 disponíveis, 7 ocupados)

2 - Reserva de um assento: se o assento estiver disp. ele vira ocup. Se estiver ocup, deve surgir um aviso no tela;

3 - Cancelar uma reserva e transformar esse assento em disponível;

4 - Reservar mais de um assento, mostrando uma lista de assentos disponíveis pela quantidade que o usuário solicitar

5 - Mostrar mapa e dados do ônibus após a reserva ( total de assentos, disponíveis, ocupados 
    e reservados naquela operação) 

6 - Permitir que o usuário saia do programa. 

"""


def dicionario_bus(livres, ocupados):
    bus = {livres: "disp" for livres in range(1, livres + 1)}
    for assento in random.sample(list(sorted(bus.keys())), ocupados):
        bus[assento] = "ocup"
    return bus


def fazer_fileiras(bus):
    contador_assentos = 0
    mapa = []
    fileira = []
    for c, v in sorted(bus.items()):
        fileira.append((c, v))
        contador_assentos += 1
        if contador_assentos % 4 == 0:
            mapa.append(fileira)
            fileira = []
    if len(fileira) > 0:
        mapa.append(fileira)
    return mapa


def texto_assento(assento):
    if assento[1] == 'disp':
        texto = f"{assento[0]:02d}, 'disp'"
    else:
        texto = f"{assento[0]:02d}, 'ocup'"
    return texto


def mostrar_mapa(bus):
    assentos = fazer_fileiras(bus)
    for fileira in assentos:
        if len(fileira) == 4:
            a1, a2, a3, a4 = fileira
            a1 = texto_assento(a1)
            a2 = texto_assento(a2)
            a3 = texto_assento(a3)
            a4 = texto_assento(a4)
            print(f'{a1} {a2}    {a4} {a3}')
        else:
            a1, a2 = fileira
            a1 = texto_assento(a1)
            a2 = texto_assento(a2)
            print(f"{a1} {a2}     WC")
            print("legenda:\n ocup = ocupado \n disp = disponível.\n  WC = Banheiro\n ")


def menu_principal():
    while True:
        print("Bem-vindo(a) ao sistema de reserva de Passagens da Viação União Santa Cruz.")
        print("OS MENORES PREÇOS PARA VOCÊ:\n "
              "Escolha sua rota de viagem digitando o número correspondente:\n"
              "1) Porto Alegre -> Florianópolis, saída às 6h, no valor de R$ 19,45;\n"
              "2) Porto Alegre -> Florianópolis, saída às 16h, no valor de R$ 23,50;\n"
              "3) Porto Alegre -> Criciúma, saída às 6h, no valor de R$ 12,90;\n"
              "4) Porto Alegre -> Criciúma, saída às 16h, no valor de R$ 15,90 \n"
              "5) Criciúma -> Florianópolis, saída às 10h, no valor de R$ 7,50;\n"
              "6) Criciúma -> Florianópolis, , saída às 20h, no valor de R$ 10,50;\n"
              "7) Para sair.\n")
        try:
            rota = int(input("Digite o número de sua escolha: "))
        except ValueError:
            print("Opção inválida")
            continue
        if rota == 1 or rota == 3:
            mostrar_mapa(bus06)
            mostrar_menu_reserva(bus06)
        elif rota == 2 or rota == 4:
            mostrar_mapa(bus16)
            mostrar_menu_reserva(bus16)
        elif rota == 5:
            mostrar_mapa(bus10)
            mostrar_menu_reserva(bus10)
        elif rota == 6:
            mostrar_mapa(bus20)
            mostrar_menu_reserva(bus20)
        elif rota == 7:
            print("Obrigado por visitar o sistema de reserva de Passagens da Viação União Santa Cruz.")
            sys.exit(0)
        else:
            print("Rota não disponível.")


def mostrar_menu_reserva(bus):
    while True:
        try:
            reserva = int(input("Escolha sua rota de viagem digitando o número correspondente:\n"
                                "1) Reservar uma(1) passagem;\n"
                                "2) Reservar duas(2) ou mais passagens;\n"
                                "3) Cancelar reserva;\n"
                                "4) Para sair.\n "
                                "Digite o número de sua escolha: \n"))
        except ValueError:
            print("Opção inválida")
            continue
        if reserva == 1:
            reserva_um(bus)
        elif reserva == 2:
            reserva_varios(bus)
        elif reserva == 3:
            libera_assento(bus)
        elif reserva == 4:
            print("Obrigado por visitar o sistema de reserva de Passagens da Viação União Santa Cruz.")
            sys.exit(0)
        else:
            print("Rota não disponível.")


contador_reservas = 0


def reserva_um(bus):
    global contador_reservas
    while True:
        try:
            reserva1 = int(input("Escolha um assento disponível:  "))
        except ValueError:
            print("Assentos inválido")
            continue
        if reserva1 in bus and bus[reserva1] == 'disp':
            bus[reserva1] = 'ocup'
            print(f'Assento {reserva1} reservado!\n')
        else:
            print(f'Assento {reserva1} indisponível\n')
        contador_reservas += 1
        mostrar_dados(bus)
        menu_principal()


def libera_assento(bus):
    global contador_reservas
    while True:
        try:
            reserva1 = int(input("Qual assento você gostaria de cancelar sua reserva? "))
        except ValueError:
            print("Assento não encontrado")
            continue
        if reserva1 in bus and bus[reserva1] == 'ocup':
            bus[reserva1] = 'disp'
            print(f'A reserva do assento {reserva1} cancelada!\n')
        else:
            print(f'Não foi possível efeturar o cancelamento do assento {reserva1} \n')
        contador_reservas -= 1
        mostrar_dados(bus)
        menu_principal()


def reserva_varios(bus):
    global contador_reservas
    while True:
        try:
            assentos = int(input("Quantos assentos você gostaria de reservar? "))
        except ValueError:
            print("Quantidade de assentos inválida")
            continue
        if assentos >= 2:
            contador_assentos_disp = 0
            assentos_disp = []
            for c, v in sorted(bus.items()):
                if v == 'disp':
                    assentos_disp.append((c, v))
                    contador_assentos_disp += 1
                    if contador_assentos_disp == assentos:
                        print(f"Esses são os assentos disponíveis: {assentos_disp}")
                        for assento in assentos_disp:
                            bus[assento[0]] = "ocup"
                        print(f'Assentos {list(dict(assentos_disp).keys())} reservados!\n')
                        break
        else:
            print("Quantidade de assentos inválida\n")
        contador_reservas += assentos
        mostrar_dados(bus)
        menu_principal()


def mostrar_dados(bus):
    mostrar_mapa(bus)
    contador_disp = 0
    contador_ocup = 0
    assentos_disp = []
    assentos_ocup = []
    print(f" Total de assentos: {len(bus)}")
    for c, v in sorted(bus.items()):
        if v == 'disp':
            assentos_disp.append((c, v))
            contador_disp += 1
        else:
            assentos_ocup.append((c, v))
            contador_ocup += 1
    print(f" Total de assentos disponíveis: {len(assentos_disp)}")
    print(f" Total de assentos ocupados: {len(assentos_ocup)}")
    print(f" Total de reservas feitas: {contador_reservas}\n")


if __name__ == "__main__":
    bus06 = dicionario_bus(46, 14)
    bus16 = dicionario_bus(46, 14)
    bus10 = dicionario_bus(46, 7)   # preciso conseguir fazer que seja o bus6 - 7 reservas e não 7 novas aleatórias
    bus20 = dicionario_bus(46, 7)
    menu_principal()
