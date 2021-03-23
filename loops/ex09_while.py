#Para uma sequência matemática onde cada elemento é calculado da seguinte forma:
#1!/N! ; 2!/(N-1)!; 3!/(N-2)!; ... ; (N! / 1!)
#Crie um programa onde o usuário digite a quantidade de elementos que deseja exibir e sejam exibidos os elementos da sequência.


#Nosso problema apresenta uma série de problemas menores: precisamos calcular o fatorial do dividendo (número que será dividido), do divisor(número que dividirá), realizar a divisão e, além disso, controlar quantas divisões serão feitas. 
#O cálculo do fatorial é feito multiplicando um número por todos os inteiros positivos anteriores a ele, até 1. Logo 5! é 5x4x3x2x1 e 10! é 10x9x8x7x6x5x4x3x2x1.
#Para realizar o cálculo do fatorial de um valor qualquer, podemos contar com uma variável para o resultado que inicia valendo 1 e multiplica a si mesma pelo próximo valor, até chegar em no valor que desejamos calcular. Veja esse exemplo:
# i = 1
# resultado = 1
# whilei<valor:
# 	resultado = resultado * i
#   i = i + 1
# 

#No exemplo acima, supondo que a variável valor seja 5 e, portanto, que nosso desejo seja calcular o fatorial de 5, teremos as seguintes execuções do loop:
#1ª volta - resultado = 1 * 1
#2ª volta - resultado = 1 * 2
#3ª volta - resultado = 2 * 3
#4ª volta - resultado = 6 * 4
#5ª volta - resultado = 24 * 5 */
#Quando o loop terminar, a variável resultado valerá 120, que é o fatorial de 5

print("Hora de trabalhar com sequências")

quantidade = int(input("Quantos elementos da sequência você deseja exibir?"))
i=0
#Para controlar a quantidade de elementos que precisamos calcular e exibir, vamos criar um loop que rode n vezes. Nossa condição, portanto, será i<quantidade:
while i<quantidade:
	#Cada vez que esse loop executar, devemos calcular o dividendo, o divisor, realizar a divisão e exibir. Vamos iniciar calculando o dividendo (número de cima)

    dividendo = 1
    iFatorial = 1
    
    while iFatorial<=(i+1):
    	#Esse loop será usado para calcular o fatorial do dividendo. Isso acontecerá fazendo a multiplicação do dividendo por iFatorial e armazenado o resultado em dividendo. 

        dividendo = dividendo * iFatorial
        iFatorial = iFatorial + 1
    #Agora vamos calcular o fatorial do divisor. Isso acontecerá fazendo a multiplicação do divisor por IFatorial e armazenando o resultado em divisor
    iFatorial = quantidade - i
    divisor = 1
    while iFatorial>1:
        divisor = divisor * iFatorial
        iFatorial = iFatorial - 1
        
    #Quando chegarmos nesse ponto, já temos o nosso dividendo e nosso divisor calculados. Resta realizarmos a divisão entre eles, guardar na variável elemento e exibir:
    elemento = dividendo / divisor
    print(elemento)
    i = i + 1


