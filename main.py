from trabalho01 import zeroum, zerodois, zerotres, zeroquatro, zerocinco, zeroseis, zerosete, zerooito, zeronove, zerodez
from trabalho02 import atv01, atv02
print("Trabalho em Python Aula 02 - Lista Sequencial\n")

def menu_principal():
    print("\nEscolha qual trabalho deseja executar\n 1 - para Lista Sequencial\n 2 - para Condicionais\n 3 - Para sair\n")
    opcao_principal = int(input("Escolha uma opção: "))
    2
    if opcao_principal == 1:
        menu_1()
    elif opcao_principal == 2:
        menu_2()
    elif opcao_principal == 3:
        exit()
    else:
        print("\nEscolha uma opção válida")
        menu_principal()

def menu_1():
    print("\nEscolha qual exercicio deseja executar 1-10\nDigite 11 Para Sair\n")
    opcao = int(input("Escolha um exercicio: "))

    if opcao == 1:
        zeroum()
        menu_1()

    elif opcao == 2:
        numero = input("Digite um numero: ")
        zerodois(numero)
        menu_1()

    elif opcao == 3:
        nota1 = input("Digite a primeira nota: ")
        nota2 = input("Digite a segunda nota: ")
        nota3 = input("Digite a terceira nota: ")
        nota4 = input("Digite a quarta nota: ")
        zerotres(nota1, nota2, nota3, nota4)
        menu_1()

    elif opcao == 4:
        num = input("Digite uma medida em metro(m): ")
        zeroquatro(num)
        menu_1()

    elif opcao == 5:
        raio = input("Digite o raio do circulo: ")
        zerocinco(raio)
        menu_1()

    elif opcao == 6:
        lado = input("Digite o lado do quadrado: ")
        zeroseis(lado)
        menu_1()

    elif opcao == 7:
        valor_hora = input("Digite o valor da hora de trabalho: ")
        horas = input("Digite as horas trabalhadas: ")
        zerosete(valor_hora, horas)
        menu_1()

    elif opcao == 8:
        temp = input("Digite a temperatura em graus Fahrenheit: ")
        zerooito(temp)
        menu_1()

    elif opcao == 9:
        inteiro1 = input("Digite o primeiro inteiro: ")
        inteiro2 = input("Digite o segundo inteiro: ")
        real = input("Digite o terceiro real: ")
        zeronove(inteiro1, inteiro2, real)
        menu_1()

    elif opcao == 10:
        altura = input("Digite sua altura(metro): ")
        zerodez(altura)
        menu_1()

    elif opcao == 11:
        exit()
    else:
        print("\nEscolha uma opção válida")
        menu_1()


def menu_2():
    print("\nEscolha qual exercicio deseja executar 1-2\nDigite 3 Para Sair\n")
    opcao = int(input("Escolha um exercicio: "))

    if opcao == 1:
        time1 = input("Digite o primeiro time: ")
        time2 = input("Digite o segundo time: ")
        gols1 = input("Digite o gols do primeiro time: ")
        gols2 = input("Digite o gols do segundo time: ")

        atv01(time1, time2, gols1, gols2)
        menu_2()
    elif opcao == 2:       
        atv02()


menu_principal()
