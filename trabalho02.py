'''
Atividade 01:
Crie um algoritmo que peça o nome de dois times de futebol e quantos gols cada time fez na partida.
Com os dados coletados, informe qual time venceu, qual time perdeu ou se houve empate.

Atividade 02:
Solicite ao usuário a resposta (sim ou não) às perguntas abaixo
e imprima a conclusão.
1) Febre alta?
2) Dores de cabeça?
3) Dores musculares?
4) Manchas vermelhas na pele?

Conclusões:
a) Se o usuário responder sim a pelo menos três perguntas,
informe que ele está com
dengue e peça para ele procurar um médico.
b) Se o usuário responder sim a duas ou menos, informe que ele deve
 ficar em repouso e continuar observando a evolução dos sintomas.

DICA: Será necessário utilizar INCREMENTO.
'''

def atv01(time1, time2, gols1, gols2):
    if gols1 > gols2:
        print(f"{time1} venceu")
    elif gols1 < gols2:
        print(f"{time2} venceu")
    else:
        print("Empate")
    return

def atv02():

    perguntas = ["Febre alta?","Dores de cabeça?","Dores musculares?","Manchas vermelhas na pele?"]
    lista = []
    for p in perguntas:
        print("Responda 'S' para sim e 'N' para não")
        valor = input(f"{p} \n")
        if valor.lower() == 's':
            lista.append(1)
            
    return print("\nO usuário está com dengue, procure um médico") if sum(lista) >= 3 else print("\nO usuário deve ficar em repouso e continuar observando a evolução dos sintomas")