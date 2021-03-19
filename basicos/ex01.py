#Para um ano de nascimento fornecido pelo usuário, informe a idade que ele terá no dia 31 de dezembro de 2021.

#é preciso, inicialmente, solicitar ao usuário seu ano de nascimento através do input, converter para número inteiro e armazenar em uma variável
nascimento = int(input("Por favor, informe seu ano de nascimento"))

#para calcular a idade, subtraímos o ano de nascimento de 2021 e armazenamos na variável idade. Para uma versão do programa que puxe o ano diretamente do sistema, consulte o arquivpo ex01v2
idade = 2021 - nascimento

#para exibir a idade do usuário, utilizamos o print para exibir um texto e o format para incluir a variável dentro desse texto
print("A sua idade no dia 31 de dezembro de 2021 será {}".format(idade))