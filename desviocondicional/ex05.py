#Um drone de limpeza de ruas deve escolher carregar sempre o lixo de menor peso. Entre os pesos de 3 lixos informados pelo usuário, um programa deve indicar qual deles deve ser carregado pelo drone.

lixo1 = float(input("Informe o peso do lixo 1"))
lixo2 = float(input("Informe o peso do lixo 2"))
lixo3 = float(input("Informe o peso do lixo 3"))

if lixo1<lixo2 and lixo1<lixo3:
    print("O lixo 1 é o lixo mais leve e será carregado")
elif lixo2<lixo1 and lixo2<lixo3:
    print("O lixo 2 é o lixo mais leve e será carregado")
elif lixo3<lixo1 and lixo3<lixo2:
    print("O lixo 3 é o lixo mais leve e será carregado")
else:
    print("Existem lixos com o mesmo peso. Contate o suporte")


