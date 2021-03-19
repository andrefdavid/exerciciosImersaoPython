#Uma loja oferece um desconto de 3% aos clientes que tiverem o cupom “DIADEFESTA”. Faça um programa onde o funcionário digite o valor da compra e um cupom, informando o valor final a ser pago.

#primeiro solicitaremos ao usuário que digite o total da compra através do input, convertendo o valor para o tipo float
total_compra = float(input("Informe o total da compra"))

#depois, pediremos que o usuário digite o cupom
cupom = input("Informe o seu cupom")

valor_final = total_compra

#Para sabermos se devemos aplicar o desconto, será necessário utilizar um desvio condicional para verificar o cupom
if "DIADEFESTA" in cupom.upper():
    valor_final = total_compra * 0.97

print("O valor original da compra era {} e após a aplicação do cupom {} passou a ser {}".forma(total_compra, cupom, valor_final))