#este codigo invertera uma string para saber se ela é um palindromo ou nao, usando o comando [::-1]
frase = str(input("digite a frase: ")).strip().lower()
palin = frase[::-1]
if frase == palin:
    print("a frase é um palindromo")
else:
    print("nao é um palindromo")
