saida = ''

def adicao(a, b):
    return a + b

def subracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

def calculadora(num1, num2, operacao):
    operacao = operacao.lower()  

    if operacao in ['+', 'adicao', 'adição', 'soma']:
        resultado = adicao(num1, num2)
    elif operacao in ['-', 'subracao', 'subtração', 'menos']:
        resultado = subracao(num1, num2)
    elif operacao in ['*', 'multiplicacao', 'multiplicação', 'x', 'vezes']:
        resultado = multiplicacao(num1, num2)
    elif operacao in ['/', 'divisao', 'divisão', 'dividir']:
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida.'

    return resultado

while saida.lower() != 'n':
    try:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        operacao = input('Digite a operação (+, -, *, /) ou o nome da operação: ')

        resultado = calculadora(num1, num2, operacao)
        print('Resultado da operação:', resultado)
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    saida = input('Deseja continuar? (S/N): ').strip().lower()
    while saida not in ['s', 'n']:
        saida = input('Resposta inválida. Digite S para continuar ou N para sair: ').strip().lower()

print('Programa encerrado.')