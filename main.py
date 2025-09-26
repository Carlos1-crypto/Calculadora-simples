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
    print("Gostaria de usar o conversor de temperatura?")
    resposta = input()
    resposta_validacao(resposta)

def resposta_validacao(resposta):
    if resposta == 's' or resposta == 'S' or resposta == 'sim' or resposta == 'Sim':
        print("Iniciando o conversor de temperatura.")
        conversor_temperatura()
    elif resposta == 'n' or resposta == 'N' or resposta == 'não' or resposta == 'Não':
        print("Ok. Até mais!")
        exit()
    else:
        print("Resposta inválida. Tente 's' e 'n'.")
        pedido_conversor()

def validar_operacao(operacao) -> int:
    if operacao == 5 or operacao == '5':
        print("Saindo da calculadora.")
        pedido_conversor()
    elif operacao in [1, 2, 3, 4, '1','2','3','4']:
        em_funcionamento(operacao)
    else:
        error(operacao)



def em_funcionamento(operacao):
    print("Você escolheu a operação ", (operacao), ".")
    print("Digite os números:")
    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))

    if (num1) == float or (num2) == float or (num1) == int or (num2) == int:
        pass

    if operacao == 1:
        print("Resultado:", soma(num1, num2))
    elif operacao == 2:
        print("Resultado:", subtracao(num1, num2))
    elif operacao == 3:
        print("Resultado:", multiplicacao(num1, num2))
    elif operacao == 4:
        print("Resultado:", divisao(num1, num2))
    else:
        print("Operação inválida.")
        em_funcionamento(operacao)
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
    operacao = int(input("Escolha a opção: "))
    if operacao == 1:
        C_F()
        pedido_conversor()
    elif operacao == 2:
        F_C()
        pedido_conversor()
    elif operacao == 3:
        sair_conversor()
    else:
        print("Opção inválida. Tente novamente.")
        conversor_temperatura()

def dnv():
    print("Gostaria de realizar outra operação? (s/n)")
    resposta = input()
    if resposta == 's' or resposta == 'S':
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        operacao = int(input("Escolha a operação: "))
        if operacao not in [5,4,3,2,1]:
            print("Opção inválida. Tente novamente.")
            dnv()
        elif operacao in [5,4,3,2,1]:
            operacao = int(operacao)
            em_funcionamento(operacao)
            # validar_operacao(operacao)
    elif resposta == 'n' or resposta == 'N':
        pedido_conversor()
    else:
        print("Resposta inválida. Tente 's' e 'n'.")
        dnv()

def error(operacao):

    if operacao == 5:
        print("Saindo da calculadora.")
        pedido_conversor()
    elif operacao in [1, 2, 3, 4]:
        em_funcionamento(int(operacao))
    elif operacao not in [1, 2, 3, 4, 5]:
        print("Opção inválida. Tente novamente.")
        a = int(input("Escolha a operação: "))
        error(a)

print("Bem Vindo à Calculadora Simples!!!!")

print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Sair")

operacao = int(input("Escolha a operação: "))
validar_operacao(operacao)
