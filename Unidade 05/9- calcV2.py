def soma(num1, num2):
    return num1 + num2
def subtracao(num1, num2):
    return num1 - num2
def multiplicacao(num1, num2):
    return num1 * num2
def divisao(num1, num2):
    return num1 / num2
def verifica_conta(conta_enviada):
    print(type(conta_enviada))
    if "+" in conta_enviada:
        nova_conta = conta_enviada.split("+")
        numero1=float(nova_conta[0])
        numero2=float(nova_conta[1])
        return soma(numero1, numero2)
    elif "-" in conta_enviada:
        nova_conta = conta_enviada.split("-")
        numero1=float(nova_conta[0])
        numero2=float(nova_conta[1])
        return subtracao(numero1, numero2)
    elif "*" in conta_enviada:
        nova_conta = conta_enviada.split("*")
        numero1=float(nova_conta[0])
        numero2=float(nova_conta[1])
        return multiplicacao(numero1, numero2)
    elif "x" in conta_enviada:
        nova_conta = conta_enviada.split("x")
        numero1=float(nova_conta[0])
        numero2=float(nova_conta[1])
        return multiplicacao(numero1, numero2)
    elif "/" in conta_enviada:
        nova_conta = conta_enviada.split("/")
        numero1=float(nova_conta[0])
        numero2=float(nova_conta[1])
        return divisao(numero1, numero2)

print("-------------------------Calculadora-------------------------")
while (True):
    resultado = verifica_conta(input("Digite a sua conta: "))
    print(resultado)
