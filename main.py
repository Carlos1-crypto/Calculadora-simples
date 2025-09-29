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

# Função principal para o funcionamento da calculadora
def em_funcionamento(operacao):
    # Pedido para o usuário escolher qual operação matemática deseja
    print("Você escolheu a operação ", (operacao), ".")
    # Pedido para o usuário escolher os 2 que quer utilizar para realizar a operação
    print("Digite os números:")
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))

    # Condição para a operação ser soma
    if operacao == 1:
        print("Resultado:", soma(num1, num2))
    # Condição para a operação ser subtração
    elif operacao == 2:
        print("Resultado:", subtracao(num1, num2))
    # Condição para a operação ser multiplicação
    elif operacao == 3:
        print("Resultado:", multiplicacao(num1, num2))
    # Condição para a operação ser divisão
    elif operacao == 4:
        print("Resultado:", divisao(num1, num2))
    # Condição para qualquer outra resposta que seja dada
    else:
        # Indicador de erro
        print("Operação inválida.")
        # Indicador de loop para o usuário tentar novamente
        em_funcionamento(operacao)
    # Chamada da função dnv caso o usuário queira tentar de novo
    dnv()

# Função que transforma Celsius em Fahrenheit
def C_F():
    # Pedido de graus Celsius
    graus = float(input("Digite a temperatura em Celsius: "))
    # Cálculo conversor
    Fahrenheit = (graus * 1.8) + 32
    # Código para retornar a resposta com o texto descritivo
    return print(graus, "Graus Celsius em Fahrenheit é: ", Fahrenheit)

# Função que transforma Fahrenheit em Celsius
def F_C():
    # Pedido de graus Fahrenheit
    graus = float(input("Digite a temperatura em Fahrenheit: "))
    # Cálculo conversor
    Celsius = (graus - 32) * 5 / 9
    # Código para retornar a resposta com o texto descritivo
    return print(graus, "Graus Fahrenheit em Celsius: ", Celsius)

# Função para saída do conversor
def sair_conversor():
    # Indicador de saída do conversor
    print("Saindo do conversor de temperatura. Até mais!")
    # --FIM DO PROGRAMA--
    exit()

# Função principal para o funcionamento do conversor de temperatura
def conversor_temperatura():
    # Bem vindas ao conversor de temperatura
    print("Bem Vindo ao Conversor de Temperatura!!!!")
    # Opções possíveis de escolha para o usuário
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Sair")
    # Decisão do usuário de qual função deseja utilizar
    operacao = int(input("Escolha a opção: "))
    # Condição necessária para converter Celsius para Fahrenheit
    if operacao == 1:
        # Chamada da função de Celsius para Fahrenheit
        C_F()
        # Chamada da função pedido_conversor caso o usuário deseje utilizar o conversor novamente
        pedido_conversor()
    # Condição necessária para converter Fahrenheit para Celsius
    elif operacao == 2:
        # Chamada da função de Fahrenheit para Celsius
        F_C()
        # Chamada da função pedido_conversor caso o usuário deseje utilizar o conversor novamente
        pedido_conversor()
    # Condição necessária para o usuário sair do pedido_conversor
    elif operacao == 3:
        # Chamada da função que finaliza o programa
        sair_conversor()
    # Condição para qualquer outra resposta que seja dada
    else:
        # Indicador de resposta inválida
        print("Opção inválida. Tente novamente.")
        # Chamada da função conversor_temperatura para o usuário tentar novamente
        conversor_temperatura()

# Função de repetição da calculadora
def dnv():
    # Pergunta se outra operação será realizada
    print("Gostaria de realizar outra operação?")
    # Resposta do usuário
    resposta = input()
    # Condições para validar a resposta que abrange várias possibilidades sinônimas ou refentes a sim
    if resposta == 's' or resposta == 'S' or resposta == 'sim' or resposta == 'Sim' or resposta == 'SIM':
        # Opções possíveis de escolha para o usuário
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        # Decisão do usuário de qual função deseja utilizar
        operacao = int(input("Escolha a operação: "))
        # Condição para caso a decisão do usuário não seja válida
        if operacao not in [5, 4, 3, 2, 1]:
            # Indicador que a resposta do usuário não foi aceita
            print("Opção inválida. Tente novamente.")
            # Chamada da função dnv para repetir até o usuário escolher uma resposta válida
            dnv()
        # Condição para casa a decisão do usuário seja válida
        elif operacao in [5, 4, 3, 2, 1]:
            # Chamada da função validar_operacao que cria para qual caminho o usuário seguirá dependendo de sua resposta
            validar_operacao(operacao)
    # Condições para validar a resposta que abrange várias possibilidades sinônimas ou refentes a não
    elif resposta == 'n' or resposta == 'N' or resposta == 'não' or resposta == 'Não' or resposta == 'NAO' or resposta == 'nao' or resposta == 'NÃO' or resposta == 'Nao':
        # Chamada da função pedido_conversor para caso o usuário não queira utiliar mais a calculadora
        pedido_conversor()
    # Condição para qualquer outra resposta que seja dada
    else:
        # Indicador de resposta inválida
        print("Resposta inválida. Tente 'sim' ou 'não'.")
        # Chamada da função dnv para o usuário tentar de novo
        dnv()

# Função error que é ativada caso o usuário escolha sair da calculadora ou dê uma resposta inválida
def error(operacao):
    # Condição necessária para sair da calculadora
    if operacao == 5:
        # Indicador de saída da calculadora
        print("Saindo da calculadora.")
        # Chamada da função pedido_conversor para perguntar o usuário se ele gostaria de usar o conversor de temperatura
        pedido_conversor()
    # Condição necessária para ativar a calculadora logo após o usuário dar uma resposta inválida
    elif operacao in [1, 2, 3, 4]:
        # Chamada da função em_funcionamento que ativa a calculadora utilizando a resposta dada do usuário
        em_funcionamento(int(operacao))
    # Condição para qualquer outra resposta que seja dada
    elif operacao not in [1, 2, 3, 4, 5]:
        # Indicador de resposta inválida
        print("Opção inválida. Tente novamente.")
        # Decisão do usuário de qual função deseja utilizar
        a = int(input("Escolha a operação: "))
        # Chamada da função error para dar a segunda chance do usuário acertar as respostas válidas
        error(a)

# --COMEÇO DO PROGRAMA--
# Bem vindas ao conversor de temperatura
print("Bem Vindo à Calculadora Simples!!!!")

# Opções possíveis de escolha para o usuário
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Sair")
# Decisão do usuário de qual função deseja utilizar
operacao = int(input("Escolha a operação: "))
# Chamada da função validar_operacao utilizando a resposta operacao dada pelo o usuário
validar_operacao(operacao)

# Fim do código.
