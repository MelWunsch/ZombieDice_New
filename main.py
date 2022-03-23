# -*- coding: utf-8 -*-
import random
print ("Bem vindo ao jogo Zombie Dice!")
comecarJogo = input("Pronto para começar a jogar ZombieDice? (S/N)\n")
if comecarJogo.lower() != "s":
    regras = input("Precisa reler as regras? Posso te passar um link.(S/N)\n")
    if regras.lower() == "s":
        print ("https://drive.google.com/file/d/1gUHl5aH9bTcp7JpcYiwhWKfq2BG9Niu3/view?usp=sharing")


numero_jogadores = int(input("Quantas pessoas vão jogar?\n"))
while numero_jogadores < 2:
    numero_jogadores = int(input("No minimo 2 jogadores. Quantos jogaores?"))

lista_jogadores = []
for i in range (numero_jogadores):
    nome = input("Qual o nome do {}º jogador?" .format(i+1))
    lista_jogadores.append(nome)

print ("\nOkay. Lembrando que temos 6 verdes (mais faceis), 4 amarelos (meio termo) e 3 vermelhos (mais difíceis). And may the odds be ever in your favor.\n")

dado_verde = "CPCTPC"
dado_amarelo = "TPCTPC"
dado_vermelho = "TPTCPT"

lista_dados = [dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde,
               dado_amarelo, dado_amarelo, dado_amarelo, dado_amarelo,
               dado_vermelho, dado_vermelho, dado_vermelho]

tiros = 0
passos = 0
cerebros = 0

dados_sorteados = []
jogador_atual = 0

while (True):
    print ("Vez dx jogadorx", lista_jogadores[jogador_atual])
    for i in range(0,3):
        nummero_sorteado = random.randint(0,12)
        dado_sorteado = lista_dados[nummero_sorteado]
        dados_sorteados.append(dado_sorteado)
        if dado_sorteado == "CPCTPC":
            cor_dado = "Verde"
        elif dado_sorteado == "TPCTPC":
            cor_dado = "Amarelo"
        else:
            cor_dado = "Vermelho"
        print ("O seu dado sorteado é da cor {}." .format(cor_dado))

    print ("\nAgora vamos ver qual face você sorteou: \n")
    for dado_sorteado in dados_sorteados:
        numero_face_dado = random.randint(0,5)
        if dado_sorteado[numero_face_dado] == "C":
            print ("Céééééérebro!!!")
            cerebros = cerebros + 1
        elif dado_sorteado[numero_face_dado] == "T":
            print ("POW! Levou um tiro.")
            tiros = tiros + 1
        else:
            print ("Passos cada vez mais longe, fugiu.")
            passos = passos + 1

    print ("\nVamos ver como está o seu score:")
    print ("Cérebros: {}\nTiros: {}\nPassos:{}\n" .format(cerebros, tiros, passos))
    continuar_partida = input("Quer continuar jogando os dados ou vamos para o próximo kogador? (S para sim e N para não)")
    if continuar_partida.lower() == "n":
        jogador_atual = jogador_atual + 1
        dados_sorteados = []
        cerebros = 0
        tiros = 0
        passos = 0
        print ("_____________________________")
    else:
        print ("Continuando então o turno atual")
        dados_sorteados = []
        print ("_____________________________")
