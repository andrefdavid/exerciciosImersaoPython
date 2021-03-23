# Um professor quer saber quantos alunos de uma sala de 50 tiveram nota maior do que a média. Faça um programa onde o professor informe a média e as notas de cada um dos 50 alunos e, ao final, seja exibido quantos alunos tiveram nota superior à média e quantos tiveram nota inferior à média.


media = float(input("Por favor, digite a média da instituição"))


acima = 0
abaixo = 0
for alunos in range(1,50,1):
    nota = float(input("Por favor, digite a nota do aluno"))

    if nota < media:
        #Aqui escrevo o que acontece se a nota for menor que a média
        abaixo = abaixo + 1
    else:
        #Aqui escrevo o que acontece se a nota for MAIOR do que a média
        acima = acima + 1

print("Para essa turma, temos {} alunos acima da média de {}".format(acima, media))
print("Para essa turma, temos {} alunos abaixo da média de {}".format(abaixo, media))