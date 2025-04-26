#um programa que criava um numero aleatorio, pro usuario acertar, falava se o numero era maior ou menor doq ele chutasse, falava se o numero era impar ou par, tentativas limitadas.
import random 
na = random.randint(0,100)
tent = 0
if na % 2 == 0:
    print('DICA: o numero aleatorio é par')
else:
    print('DICA: o numero aleatorio é impar')
while True:
    try:
        chute = int(input('digite o seu chute: '))
        if chute < 0:
            print('tente um numero positivo!!')
            continue
        tent += 1
        print('essa foi sua tentativa de numero: ',tent)
        if tent == 10:
            print('acabou as tentativas')
            break
        if chute > na:
            print('o numero aleatorio é menor')
        elif chute < na:
            print('o numero aleatorio é maior')
        else:
            print('voce acertou o numero, PARABENS')
            break
    except ValueError:
        print('digite um número inteiro.')
