#importação das Bibliotecas
import os
import time
import random

#variaveis globais
cont1 = 0   
cont2 = 0
num = random.randint(0,100)


#Função para saudar os jogadores
def saudacao():
    print("\nBem-vindos ao jogo de adivinhação!\n")
    print("Regras do jogo:\n")
    print("1. O computador escolherá um número aleatório entre 0 e 100.")
    print("2. Dois jogadores irão se revezar para tentar adivinhar o número.")
    print("3. Digite apenas números inteiros.")
    print("4. Receberão dicas de 'maior' ou 'menor' para ajustar suas tentativas.")
    print("5. Vence quem acertar o número primeiro!")
    print("Boa sorte!")

    input("\nClique em qualquer tecla para continuar...\n")
    os.system('cls')  # limpa o terminal após a saudação

#função jagador 1
def jogador1():
    global cont1
    global num
    cont1 = cont1 + 1

    print("Jogador numero 1 joga")
    tentativa = int(input("Digite sua tentativa: "))
    if tentativa == num:
        return tentativa
    if tentativa > num:
        print("Na sua proxima vez, digite um numero menor")
    else:
        print("Na sua proxima vez, digite um numero maior")

    time.sleep(3) #função para gerar um delay antes de limpar o terminal
    os.system('cls') #função para limpar o terminal
    return tentativa

#Função jogador 2
def jogador2():
    global cont2
    global num
    cont2 = cont2 + 1

    print("Jogador numero 2 joga")
    tentativa = int(input("Digite sua tentativa: "))
    if tentativa == num:
        return tentativa
    if tentativa > num:
        print("Na sua proxima vez, digite um numero menor")
    else:
        print("Na sua proxima vez, digite um numero maior")
    

    time.sleep(3)  #função para gerar um delay antes de limpar o terminal
    os.system('cls') #função para limpar o terminal
    return tentativa


#Função que executa o jogo
def jogo():
    saudacao()
    while True:
        if jogador1() == num:
            print(f'Jogador numero 1 ganhou, em sua {cont1}° tentativa')
            time.sleep(3)
            break

        if jogador2() == num:
            print(f'Jogador numero 2 ganhou, em sua {cont2}° tentativa')
            time.sleep(3)
            break



#chamando a função jogo(), para excutar o game 
jogo()
