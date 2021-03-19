#Sabendo que cada hora dura 60 minutos e que cada minuto dura 60 segundos, solicite ao usuário que digite o tempo de um filme em minutos e informe a duração desse filme em horas e em segundos.

#primeiro, solicitamos ao usuário a duração do filme em minututos, usando o input e convertendo o valor para um número inteiro
minutos = int(input("Informe a duração do filme em minutos"))

#para calcular as horas, dividimos a duração em minutos por 60
horas = minutos/60

#para calcular os segundos, multiplicamos a duração do filme por 60
segundos = minutos * 60

#Agora precisamos apenas exibir os resultados
print("O filme que dura {} minutos, tem {} horas ou ainda {} segundos de duração".format(minutos, horas, segundos))