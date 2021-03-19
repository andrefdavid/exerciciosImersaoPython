#Um robô de combate só deve ativar sua arma principal quando o inimigo está a menos de 70cm de distância. Faça um programa onde o usuário informe a distância do inimigo e sejam exibidas as mensagens “ATIVADO” ou “DESATIVADO” dependendo do status da arma.

distancia = float(input("Digite a distância do inimigo"))

if distancia < 70:
    print("ARMA ATIVADA")
else:
    print("ARMA DESATIVADA")