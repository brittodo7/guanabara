valor1 = float(input("digite o valor do primeiro numero :"))
valor2 = float(input("digite o valor do segundo numero :"))
soma = valor1 + valor2
print (f"o resultado da soma é {soma}")

valor1 = float(input("digite o valor do primeiro numero :"))
valor2 = float(input("digite o valor do segundo numero :"))
valor3 = float(input("digite o valor do terceiro numero :"))
media = valor1 + valor2 + valor3 / 3
print (f"o resultado da media é {media}")

valor1 = float(input("digite o valor da base :"))
valor2 = float(input("digite o valor da altura :"))
media = valor1 * valor2
print (f"o resultado da area é {media}")

valor1 = float(input("digite o valor em celsius :"))
media = valor1 * 1.8 +32
print (f"o resultado da conversao é {media}")

valor1 = float(input("digite seu peso :"))
valor2 = float(input("digite sua altura :"))
media = valor1 / (valor2*valor2)
print (f"o resultado do seu imc é {media}")

valor1 = float(input("digite um numero :"))
dobro = valor1 * 2
triplo = valor1 * 3
print (f"o resultado do dobro é {dobro} e o resultado do triplo é {triplo}")

valor1 = float(input("digite o preco do produto :"))
valor2 = float(input("digite o valor do desconto :"))
soma = valor1  * valor2 / 100
print (f"o resultado do seu desconto é {soma}")

valor1 = float(input("digite o seu salario :"))
valor2 = float(input("digite o seu aumento:"))
soma = valor1  * valor2 + valor1
print (f"o salario é {soma}")

valor1 = float(input("digite um valor em real :"))
dobro = valor1 / 5.70
print (f"o resultado da conversao é {dobro}")

valor1 = float(input("digite um numero :"))
valor2 = float(input("digite outro numero: "))
soma = valor1 + valor2
sub = valor1 - valor2
multi = valor1* valor2
div = valor1/valor2
print (f"o resultado da soma é {soma} e o resultado do subtração é {sub} o resultado da multiplicação é {multi} o resultado da divisao é {div}")

valor1 = float(input("digite o primeiro valor"))
valor2 = float(input("digite o segundo valor"))
quo = divmod (valor1, valor2)
print (f"o quociente e resto é {quo}")

valor1 = float(input("digite o primeiro valor :"))
valor2 = float(input("digite o segundo valor :"))
media = pow (valor1,valor2)
print (f"o resultado da potencia é {media}")

valor1 = float(input("digite um valor :"))
dobro = valor1 ** 0.5
print (f"o resultado da raiz é {dobro}")

def somar_algarismos(numero):
    digito1 = numero // 10
    digito2 = numero % 10
    return digito1 + digito2
numero1 = int(input("Digite o primeiro número de dois dígitos: "))
numero2 = int(input("Digite o segundo número de dois dígitos: "))
soma1 = somar_algarismos(numero1)
soma2 = somar_algarismos(numero2)
print(f"A soma dos algarismos do primeiro número ({numero1}) é: {soma1}")
print(f"A soma dos algarismos do segundo número ({numero2}) é: {soma2}")

hora = float(input("Digite um valor em horas :"))
minutos = hora * 60
seg = hora * 3600
print (f"{hora} horas em segundos fica {seg} segundos e em minutos {minutos} minutos")

import math
x1, y1 = map(float, input("Digite as coordenadas do primeiro ponto (x1, y1) separadas por espaço: ").split())
x2, y2 = map(float, input("Digite as coordenadas do segundo ponto (x2, y2) separadas por espaço: ").split())
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print (f" a distancia entre os dois pontos é de {d}")

capital = float(input("digite seu capital :"))
juros = float(input("digite o juros em numeros decimais :"))
tempo = float(input("digite o tempo em anos"))
s = capital * juros * tempo + capital
print (f" o total do juros simples ficou {s}")

numero = float(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

seg = float(input("Digite um valor em segundos :"))
minutos = seg / 60
hora = seg / 3600
print (f"{seg} segundos em minutos fica {minutos} min e em horas {hora} hs")
