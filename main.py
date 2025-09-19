def soma(a, b):
    soma = a + b
    return soma

def subtracao(a, b):
    subtracao = a - b
    return subtracao

def multiplicacao(a, b):
    multiplicacao = a * b
    return multiplicacao

def divisao(a, b):
    if b != 0:
        divisao = a / b
        return divisao
    else:
        return "Divisão por zero não é permitida."


def pedido_conversor():
    print("Gostaria de usar o conversor de temperatura? (s/n)")
    resposta = input()
    if resposta == 's' or resposta == 'S':
        conversor_temperatura()
    elif resposta == 'n' or resposta == 'N':
        print("Ok. Até mais!")
        exit
    else:
        print("Resposta inválida. Tente 's' e 'n'.")
        pedido_conversor()

def em_funcionamento(a):
    print("Você escolheu a operação ", (a), ".")
    print("Digite os números:")
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
    if o == 1:
        print("Resultado: ", soma(num1, num2))
    elif o == 2:
        print("Resultado: ", subtracao(num1, num2))
    elif o == 3:
        print("Resultado: ", multiplicacao(num1, num2))
    elif o == 4:
        print("Resultado: ", divisao(num1, num2))

    dnv()
    
def C_F():
    graus = float(input("Digite a temperatura em Celsius: "))
    Fahrenheit = (graus * 1.8) + 32
    return print(graus, "Graus Celsius em Fahrenheit é: ", Fahrenheit)
    
def F_C():
    graus = float(input("Digite a temperatura em Fahrenheit: "))
    Celsius = (graus - 32) * 5 / 9
    return print(graus, "Graus Fahrenheit em Celsius: ", Celsius)

def sair_conversor():
    print("Saindo do conversor de temperatura. Até mais!")
    exit()

def conversor_temperatura():
    print("Bem Vindo ao Conversor de Temperatura!!!!")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Sair")
    operacao = input("Escolha a opção: ")
    if operacao == 1 or operacao == '1':
        C_F()
        pedido_conversor()
    elif operacao == 2 or operacao == '2':
        F_C()
        pedido_conversor()
    elif operacao == 3 or operacao == '3':
        sair_conversor()
    else:
        print("Opção inválida. Tente novamente.")
        conversor_temperatura()

def dnv():
    print("Gostaria de realizar outra operação? (s/n)")
    resposta = input()
    if resposta == 's' or resposta == 'S':
        operacao = int(input("Escolha a operação: "))
        em_funcionamento(operacao)
    elif resposta == 'n' or resposta == 'N':
        pedido_conversor()
        exit()
    else:
        print("Resposta inválida. Tente 's' e 'n'.")
        dnv()

def error():
    
    operacao = input("Escolha a operação: ")
    if operacao == '5':
        print("Saindo da calculadora.")
        pedido_conversor()
    elif operacao in ['1', '2', '3', '4']:
        operacao = int(operacao)
        em_funcionamento()
        dnv()
    else:
        error()

print("Bem Vindo à Calculadora Simples!!!!")

print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Sair")


o = int(input("Escolha a operação: "))


def operacao(a) -> int:

    if a == 5:
        print("Saindo da calculadora.")
        pedido_conversor()
    elif a in [1, 2, 3, 4]:
        em_funcionamento(o)
    else:
        print("Opção inválida. Tente novamente.")
        operacao()

operacao(o)
