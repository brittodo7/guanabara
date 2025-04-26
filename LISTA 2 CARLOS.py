idade = float(input("Qual a sua idade? "))
cnh = input("Você possui CNH? (sim/não) ").strip().lower()

if idade >= 18 and cnh == "sim":
    print("Pode dirigir")

else:
    print("Não pode dirigir")


valor = float(input("Qual é o valor? "))
if 10 <= valor <= 50:
        print("o numero esta entre 10 e 50")
        
else:
        print("o numero nao esta entre 10 e 50")

valor1 = float(input("digite o primeiro valor? "))
valor2 = float(input("digite o segundo valor "))
valor3 = float(input("digite o terceiro valor "))

sum = valor1+valor2+valor3
if sum / 3 >= 7:
      print ("aprovado")
else:
      print ("reprovado")

valor1 = float(input("digite o primeiro valor? "))
valor2 = float(input("digite o segundo valor "))
if valor1 >= 0 and valor2 >= 0:
      print ("ambos sao positivos")
else: 
      print("nao sao positivos")

valor = float(input("Qual é o valor? "))
if valor % 2 == 0 and valor > 20:
      print ("numero par e maior que 20")
else:
      print("nao")

valor = float(input("digite um numero: "))
if valor > 0 :
      print ("numero positivo")
else:
      print("numero negativo")

ano = float(input("digite um ano: "))
def is_bis(ano):
      if (ano % 4 == 0) or (ano % 400 == 0):
            return True
      else:
            return False
if is_bis(ano):
      print("o ano é bisexto")
else:
      print("nao é bisexto")

idd = float(input("digite sua idade: "))
if idd >= 18:
      print("voce é de maior")
else:
      print("voce é de menor")

senha = int(input("digite a senha: ")).strip()
if senha == 1234:
      print ("acesso permitido")
else:
      print("")

num = float(input("digite um numero: "))
def mul(num):
      if num % 5 == 0:
            return True
      else:
            return False
if mul(num) :
      print ("é multiplo de 5")
else:
      print ("nao é multiplo de 5")

nota = float(input("digite sua nota: "))
if 0 <= nota <= 4:
      print("nota vermelha")
elif 5 <= nota <= 7:
      print("nota azul")
elif 8 <= nota <= 10:
      print("nota verde")
elif nota < 10:
      print("digite uma nota de 0 a 10!!!")

num = float(input("digite um numero: "))
if num > 0:
      print("numero positivo")
elif num < 0:
      print("numero negativo")
elif num == 0:
      print("numero nulo.")

def cal(val):
    if val < 50:
      desc = val * 0
      return desc
    elif 100 < val < 50:
        desc = val * 0.05
        return desc
    elif val > 100:
        desc = val * 0.1
    return desc
val = int(input("digite o valor da compra: "))
desc = cal(val)
valfin = val - desc
print("o valor ficou:", valfin)


def div(num):
      if num % 3 == 0 and num % 5 == 0:
            print ("o numero é divisivel por 3 e 5")
      elif num % 5 == 0:
            print ("numero é divisor de 5")
      elif num % 3 == 0:
            print ("numero é divisor de 3")
            return num
num = int(input("digite um numero: "))
div(num)


num1 = int(input("escreva o primeiro numero"))
num2 = int(input("escreva o segundo numero"))
num3 = int(input("escreva o terceiro numero"))
if num1 > num2 and num1 > num3:
      print(num1)
elif num2 > num1 and num2 > num3:
      print(num2)
elif num3 > num2 and num3> num1:
      print(num3)

def pi (num):
      if num & 2 ==0:
            print("o numero é par")
      else:
            print("o numero é impar")
      return pi
def mm (num):
      if num > 100:
            print("numero é maior que 100")
      else:
            print("numero é menor que 100")
      return mm
num = int(input("digite um numero: "))
(pi(num))
(mm(num))

def pm (ano):
      if ano % 2 == 0 and ano % 4 == 0:
            print ("o numero é par e multiplo de 4 ao msm tempo")
      else:
            print("o num nao é")
ano = int(input("digite um ano: "))
pm(ano)


def per (idd,alt):
      if idd >= 12 and alt >= 140:
            print ("pode entrar")
      else:
            print("nao pode")

idd = int(input("digite sua idade: "))
alt = int(input("digite sua altura em cm: "))
per (idd,alt)


a = float(input("digite um lado: "))
b = float(input("digite um lado: "))
c = float(input("digite um lado: "))


if a + b > c and a + c > b and b + c > a:
    print("pode")
else:
    print("nao pode")


def inter (num):
      if 100 > num > 0:
            print("o numero esta entre 1 e 100")
      else:
            print("o numero nao esta entre 1 e 100")
      
def primo (num):
      if num / num == 1 and num > 1 :
            print("o numero é primo")
      else:
            print("o numero nao é primo")

num = int(input("digite um numero: "))
primo (num)
inter (num)

num = int(input("insira o valor que sera sacado :"))
if num & 10 == 0:
      print(f"o valor a ser sacado {num} é multiplo de 10!")
elif num % 10 != 0:
      print(f"o valor {num} nao é multiplo de 10")


def pno(num):
      if num > 0:
            print ("numero é positivo")
      elif num < 0:
            print ("o numero é negativo")
      elif num == 0:
            print ("NULO")
def div(num):
      if num % 2 == 0:
            print("numero divisivel por 2")
      else:
            print("nao divide por 2")
num = int(input("digite um numero: "))
pno(num)
div(num)

print(" Seja Bem Vindo")
print("O nosso cardapio é:")
print("1. Salada")
print("2. Hamburguer")
print("3. Ameixa")
print("4. Copo de agua")
car = int(input("qual vc deseja?"))
if car == 1:
      print("que bom, o valor é R$10,00")
elif car == 2:
      print("que bom, o valor é R$15,00")
elif car == 3:
      print("que bom, o valor é R$20,00")
elif car == 4:
      print("que bom, o valor é R$0,00")
else:
      print("Faca uma escolha de 1 ao 4!!") 


def cal(val):
    if 4999> val > 3000:
        desc = val * 0.05
        return desc
    elif 9999 > val > 5000:
        desc = val * 0.1
        return desc
    elif val > 10000:
        desc = val * 0.15
        return desc
val = int(input("digite o valor do seu salario: "))
desc = cal(val)
valfin = val - desc
print(f"o valor ficou {valfin}")

import random
var = random.randint(0,100)
while True:
      num = int(input("digite seu chute: "))
      if num > var:
            print("o numero secreto é menor")
      elif num < var:
            print("o numero secreto é maior")
      else:
            print("acertou!!!!")
            break
