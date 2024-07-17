def soma(num1, num2):
    return num1 + num2
def subtracao(num1, num2):
    return num1 - num2
def multiplicacao(num1, num2):
    return num1 * num2
def divisao(num1, num2):
    return num1 / num2
print("--------------------------------------Calculadora--------------------------------------")
rodando = True
while (rodando):
    escolha = int(input("Selecione uma opção de calculo: \n1- Soma \n2- Subtração \n3- Multiplicação \n4- Divisão \n5- Encerrar\n"))
    if escolha == 5: 
        rodando = False
        print("Encerrando")
    elif escolha > 5 or escolha < 1:
        print("Valor incorreto")
    else:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        if escolha == 1:
            print("A soma de %.2f e %.2f é %.2f" %(num1, num2, soma(num1, num2)))
        elif escolha == 2:
            print("A subtração de %.2f e %.2f é %.2f" %(num1, num2, subtracao(num1, num2)))
        elif escolha == 3:
            print("A multiplicação de %.2f e %.2f é %.2f" %(num1, num2, multiplicacao(num1, num2)))
        else:
            print("A divisão de %.2f e %.2f é %.2f" %(num1, num2, divisao(num1, num2)))