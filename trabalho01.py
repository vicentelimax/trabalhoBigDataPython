#1) Faça um Programa que mostre a mensagem "Alo mundo" na tela.

def zeroum():
    return print("Ola mundo")

#2)Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
def zerodois(num):
    
    try:
        num = float(num)
        return print(f"O numero informado foi [{num}]")
    except ValueError:
        return print(f"Deve ser digitado um numero! [{num}] nao eh um numero")

#3) Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def zerotres(nota1, nota2, nota3, nota4):

    valores = [float(nota1), float(nota2), float(nota3), float(nota4)]
    media = sum(valores) / len(valores)

    return print(f"A media das notas eh {media}")

#4) Faça um Programa que converta metros para centímetros.
def zeroquatro(num):
    return print(f"{num} metro(s) = {float(num) * 100} centímetro(s)") #num * 100

#5) Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
def zerocinco(raio):
    return print(f"A area do circulo e {3.14 * float(raio) ** 2}")
#6) Faça um Programa que calcule a área de um quadrado
def zeroseis(lado):
    return print(f"A area do quadrado e {float(lado) ** 2}")
#7) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do 
#seu salário no referido mês.
def zerosete(valor_hora, horas):
    return print(f"O seu salario no mes foi de R$ {float(valor_hora) * float(horas)}")
#8) Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).
def zerooito(temp):
    return print(f"{temp} graus Fahrenheit = {5 * ((float(temp) - 32) / 9)} graus Celsius")

#9) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a)o produto do dobro do primeiro com metade do segundo .
#b)a soma do triplo do primeiro com o terceiro.
#c)o terceiro elevado ao cubo.
def zeronove(inteiro1, inteiro2, real):
    calculo1 = (float(inteiro1) * 2) * (float(inteiro2) / 2)
    calculo2 = (float(inteiro1) * 3) + float(real)
    calculo3 = float(real) ** 3
    return print(f"O produto do dobro do primeiro com metade do segundo eh {calculo1}\nA soma do triplo do primeiro com o terceiro eh {round(calculo2, 3)}\nO terceiro elevado ao cubo eh {round(calculo3, 3)}")

#10) Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
#usando a seguinte fórmula: (72.7*altura) - 58
def zerodez(altura):
    return print(f"Seu peso ideal eh {(72.7 * float(altura)) - 58}")