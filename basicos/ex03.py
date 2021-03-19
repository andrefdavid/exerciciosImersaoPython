#Solicite ao usuário a digitação de 2 números inteiros, nas variáveis A e B. Sem usar uma terceira variável, troque os valores de A e B entre si.
a = int(input("Digite um número inteiro"))
b = int(input("Digite outro número inteiro"))

a = a + b
b = a - b
a = a - b

print("A é {} e B é {}".format(a, b))