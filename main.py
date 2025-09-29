# Calcuyladora simples com conversor de temperatura
# Autor: Carlos Henrique Silva Prates Viana
# Data do último commit: 29/09/2025
# Versão: 1.0.0
# Linguagem: Python 3.13.6
# Repositório: https://github.com/Carlos1-crypto/Calculadora-simples
# Descrição: Uma calculadora simples que realiza operações básicas e inclui um conversor de temperatura entre Celsius e Fahrenheit.
# Instruções: Execute o script e siga as instruções no terminal para usar a calculadora e o conversor de temperatura.
# Observações: Certifique-se de ter o Python 3.13.6 instalado para executar este script.
# Feedback: Sinta-se à vontade para contribuir com melhorias ou relatar problemas no repositório do GitHub.
# Contato: 73 98801-7107
# Email: chspv2007@gmail.com
# LinkedIn: https://linkedin.com/in/carlos-viana-489b02355
# GitHub: https://github.com/Carlos1-crypto

# Início do código.
# Função de soma entre 2 números inteiros
def soma(a, b):
    soma = a + b
    return soma

# Função de subtração entre 2 números inteiros
def subtracao(a, b):
    subtracao = a - b
    return subtracao

# Função de multiplicação entre 2 números inteiros
def multiplicacao(a, b):
    multiplicacao = a * b
    return multiplicacao

# Função de divisão entre 2 números inteiros
def divisao(a, b):
    if b != 0:
        divisao = a / b
        return divisao
    else:
        return "Divisão por zero não é permitida."

# Função para pedir se o usuário gostaria de usar o conversor de temperatura
def pedido_conversor():
    print("Gostaria de usar o conversor de temperatura?")
    resposta = input()
    # Chamada da função resposta_validação com o objeto usado sendo a resposta da pergunta da função pedido_conversor
    resposta_validacao(resposta)

# Função que valida a resposta da função pedido_conversor
def resposta_validacao(resposta):
    # Condições para validar a resposta que abrange várias possibilidades sinônimas ou refentes a sim
    if resposta == 's' or resposta == 'S' or resposta == 'sim' or resposta == 'Sim' or resposta == 'SIM':
        # Mensagem para sinalizar que o que foi entendido foi uma resposta afirmativa
        print("Iniciando o conversor de temperatura.")
        # Chamada da função conversor_temperatura que é onde a(s) operação(ões) são escolhidas e os cálculos são feitos
        conversor_temperatura()
    # Condições para validar a resposta que abrange várias possibilidades sinônimas ou refentes a não
    elif resposta == 'n' or resposta == 'N' or resposta == 'não' or resposta == 'Não' or resposta == 'NAO' or resposta == 'nao' or resposta == 'NÃO' or resposta == 'Nao':
        # Mensagem para sinalizar que o que foi entendido foi uma resposta negativa
        print("Ok. Até mais!")
        # --FIM DO PROGRAMA--
        exit()
    # Excessão para qualquer outra resposta que seja dada
    else:
        # Indicador que o usuário irá tentar de novo
        print("Resposta inválida. Tente 's' e 'n'.")
        # Chamada de volta para a função pedido_conversor até que o usuário acerte alguma das opções aceitáveis de resposta
        pedido_conversor()

# Função que valida a resposta da única tupla operação que está fora de todas as funções // Expecificando que seu tipo recebido é apenas números inteiros
def validar_operacao(operacao) -> int:
    # Condição necessária para sair da calculadora
    if operacao == 5:
        # Mensagem para sinalizar que está saindo da calculadora
        print("Saindo da calculadora.")
        # Chamada da função pedido_conversor que oferece ao usuário usar o conversor de temperatura
        pedido_conversor()
    # Condições necessárias para selecionar uma das operações dadas ao usuário
    elif operacao in [1, 2, 3, 4]:
        # Chamada da função em_funcionamento para que a calculadora continue funcionando
        em_funcionamento(operacao)
    # Excessão para qualquer outra resposta que seja dada
    else:
        # Chamada da função error para qualquer outra resposta que seja dada
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

# Fim do código.