#a linha abaixo importa o pacote datetime, para recuperarmos a data do sistema operacional
from datetime import datetime

#Para um ano de nascimento fornecido pelo usuário, informe a idade que ele terá no dia 31 de dezembro de 2021.

#é preciso, inicialmente, solicitar ao usuário seu ano de nascimento através do input, converter para número inteiro e armazenar em uma variável
nascimento = int(input("Por favor, informe seu ano de nascimento"))

#para recuperarmos o ano do sistema operacional, utilizaremos a instrução datetime.now().year
ano_atual = datetime.now().year


#para calcular a idade, subtraímos o ano de nascimento do ano atual e armazenamos na variável idade.
idade = ano_atual - nascimento

#para exibir a idade do usuário, utilizamos o print para exibir um texto e o format para incluir a variável dentro desse texto
print("A sua idade no dia 31 de dezembro de {} será {}".format(ano_atual, idade))