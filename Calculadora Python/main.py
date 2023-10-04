import math

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Não é possível dividir por zero"
    return x / y

def exponenciacao(x, y):
    return x ** y

def raiz_quadrada(x):
    if x < 0:
        return "Não é possível calcular a raiz quadrada de um número negativo"
    return math.sqrt(x)

def porcentagem(x, y):
    return (x * y) / 100

def logaritmo_natural(x):
    if x <= 0:
        return "Não é possível calcular o logaritmo natural de um número não positivo"
    return math.log(x)

def logaritmo_base_10(x):
    if x <= 0:
        return "Não é possível calcular o logaritmo na base 10 de um número não positivo"
    return math.log10(x)

def fatorial(x):
    if x < 0:
        return "Não é possível calcular o fatorial de um número negativo"
    if x == 0:
        return 1
    return math.factorial(x)

def seno(x):
    return math.sin(x)

def cosseno(x):
    return math.cos(x)

def tangente(x):
    return math.tan(x)

def valor_absoluto(x):
    return abs(x)

def arredondamento(x):
    return round(x)

def potencia_de_10(x):
    return 10 ** x

def logaritmo_base_2(x):
    if x <= 0:
        return "Não é possível calcular o logaritmo na base 2 de um número não positivo"
    return math.log2(x)

def cosseno_hiperbolico(x):
    return math.cosh(x)

def tangente_hiperbolica(x):
    return math.tanh(x)

def valor_minimo(x, y):
    return min(x, y)

def valor_maximo(x, y):
    return max(x, y)

def media_aritmetica(lista):
    if len(lista) == 0:
        return "A lista está vazia"
    return sum(lista) / len(lista)

def mediana(lista):
    if len(lista) == 0:
        return "A lista está vazia"
    lista_ordenada = sorted(lista)
    meio = len(lista_ordenada) // 2
    if len(lista_ordenada) % 2 == 0:
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:
        return lista_ordenada[meio]

def desvio_padrao(lista):
    if len(lista) <= 1:
        return "Não é possível calcular o desvio padrão com menos de 2 números"
    media = sum(lista) / len(lista)
    somatorio_diferencas_quadradas = sum((x - media) ** 2 for x in lista)
    return math.sqrt(somatorio_diferencas_quadradas / (len(lista) - 1))

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def metro_quadrado_para_pe_quadrado(metro_quadrado):
    return metro_quadrado * 10.7639

def pe_quadrado_para_metro_quadrado(pe_quadrado):
    return pe_quadrado / 10.7639

def litros_para_galoes(litros):
    return litros * 0.264172

def galoes_para_litros(galoes):
    return galoes / 0.264172

def euros_para_dolares(euros, taxa_de_cambio):
    return euros * taxa_de_cambio

def dolares_para_euros(dolares, taxa_de_cambio):
    return dolares / taxa_de_cambio

def resolver_equacao_quadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "A equação não possui raízes reais"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"A única raiz real é x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"As raízes reais são x1 = {x1} e x2 = {x2}"

while True:
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Exponenciação")
    print("6. Raiz Quadrada")
    print("7. Porcentagem")
    print("8. Logaritmo Natural")
    print("9. Logaritmo na Base 10")
    print("10. Fatorial")
    print("11. Seno")
    print("12. Cosseno")
    print("13. Tangente")
    print("14. Valor Absoluto")
    print("15. Arredondamento")
    print("16. Potência de 10")
    print("17. Logaritmo na Base 2")
    print("18. Cosseno Hiperbólico")
    print("19. Tangente Hiperbólica")
    print("20. Valor Mínimo")
    print("21. Valor Máximo")
    print("22. Média Aritmética")
    print("23. Mediana")
    print("24. Desvio Padrão")
    print("25. Celsius para Fahrenheit")
    print("26. Fahrenheit para Celsius")
    print("27. Metro Quadrado para Pé Quadrado")
    print("28. Pé Quadrado para Metro Quadrado")
    print("29. Litros para Galões")
    print("30. Galões para Litros")
    print("31. Euros para Dólares")
    print("32. Dólares para Euros")
    print("33. Resolver Equação Quadrática")
    print("34. Sair")

    escolha = input("Digite o número da operação desejada (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34): ")

    if escolha == '34':
        print("Obrigado por utilizar minha aplicação. Atenciosamente, Daniel Tomazi.")
        break

    if escolha not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33'):
        print("Opção inválida. Por favor, escolha uma opção válida.")
        continue

    if escolha in ('22', '23', '24'):
        lista = []
        try:
            num_of_values = int(input("Quantos valores você deseja inserir na lista? "))
            for i in range(num_of_values):
                value = float(input(f"Digite o valor {i + 1}: "))
                lista.append(value)
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir números válidos.")
            continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = None

        if escolha != '6' and escolha != '8' and escolha != '9' and escolha != '10' and escolha != '11' and escolha != '14' and escolha != '22' and escolha != '23' and escolha != '24' and escolha != '25' and escolha != '26' and escolha != '27' and escolha != '28' and escolha != '29' and escolha != '30' and escolha != '31' and escolha != '32':
            num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números válidos.")
        continue

    if escolha == '1':
        resultado = adicao(num1, num2)
    elif escolha == '2':
        resultado = subtracao(num1, num2)
    elif escolha == '3':
        resultado = multiplicacao(num1, num2)
    elif escolha == '4':
        resultado = divisao(num1, num2)
    elif escolha == '5':
        resultado = exponenciacao(num1, num2)
    elif escolha == '6':
        resultado = raiz_quadrada(num1)
    elif escolha == '7':
        resultado = porcentagem(num1, num2)
    elif escolha == '8':
        resultado = logaritmo_natural(num1)
    elif escolha == '9':
        resultado = logaritmo_base_10(num1)
    elif escolha == '10':
        resultado = fatorial(num1)
    elif escolha == '11':
        resultado = seno(num1)
    elif escolha == '12':
        resultado = cosseno(num1)
    elif escolha == '13':
        resultado = tangente(num1)
    elif escolha == '14':
        resultado = valor_absoluto(num1)
    elif escolha == '15':
        resultado = arredondamento(num1)
    elif escolha == '16':
        resultado = potencia_de_10(num1)
    elif escolha == '17':
        resultado = logaritmo_base_2(num1)
    elif escolha == '18':
        resultado = cosseno_hiperbolico(num1)
    elif escolha == '19':
        resultado = tangente_hiperbolica(num1)
    elif escolha == '20':
        resultado = valor_minimo(num1, num2)
    elif escolha == '21':
        resultado = valor_maximo(num1, num2)
    elif escolha == '22':
        resultado = media_aritmetica(lista)
    elif escolha == '23':
        resultado = mediana(lista)
    elif escolha == '24':
        resultado = desvio_padrao(lista)
    elif escolha == '25':
        resultado = celsius_para_fahrenheit(num1)
    elif escolha == '26':
        resultado = fahrenheit_para_celsius(num1)
    elif escolha == '27':
        resultado = metro_quadrado_para_pe_quadrado(num1)
    elif escolha == '28':
        resultado = pe_quadrado_para_metro_quadrado(num1)
    elif escolha == '29':
        resultado = litros_para_galoes(num1)
    elif escolha == '30':
        resultado = galoes_para_litros(num1)
    elif escolha == '31':
        taxa_de_cambio = float(input("Digite a taxa de câmbio: "))
        resultado = euros_para_dolares(num1, taxa_de_cambio)
    elif escolha == '32':
        taxa_de_cambio = float(input("Digite a taxa de câmbio: "))
        resultado = dolares_para_euros(num1, taxa_de_cambio)
    elif escolha == '33':
        try:
            a = float(input("Digite o coeficiente a: "))
            b = float(input("Digite o coeficiente b: "))
            c = float(input("Digite o coeficiente c: "))
            resultado = resolver_equacao_quadratica(a, b, c)
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir números válidos.")
            continue

    print("Resultado:", resultado)
