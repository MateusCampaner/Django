import numpy as np
from django.shortcuts import render

# Create your views here.

def calculadora(request):
    resultado = None

    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        if 'add' in request.POST:
            resultado = num1 + num2
        elif 'subtract' in request.POST:
            resultado = num1 - num2
        elif 'multiply' in request.POST:
            resultado = num1 * num2
        elif 'divide' in request.POST:
            if num2 != 0:
                resultado = num1 / num2

    return render(request, 'calculadora.html', {'resultado': resultado})


def metodo_bolzano(request):
    raizes = []

    if request.method == 'POST':
        # Obtém os valores do formulário e define 0 como valor padrão se estiverem vazios
        a = float(request.POST.get('a', 0)) if request.POST.get('a') else 0
        b = float(request.POST.get('b', 0)) if request.POST.get('b') else 0
        c = float(request.POST.get('c', 0)) if request.POST.get('c') else 0
        d = float(request.POST.get('d', 0)) if request.POST.get('d') else 0
        e = float(request.POST.get('e', 0)) if request.POST.get('e') else 0
        f = float(request.POST.get('f', 0)) if request.POST.get('f') else 0
        g = float(request.POST.get('g', 0)) if request.POST.get('g') else 0
        h = float(request.POST.get('h', 0)) if request.POST.get('h') else 0
        i = float(request.POST.get('i', 0)) if request.POST.get('i') else 0
        j = float(request.POST.get('j', 0)) if request.POST.get('j') else 0
        a_intervalo = float(request.POST.get('a_intervalo', -10))
        b_intervalo = float(request.POST.get('b_intervalo', 10))

        # Função para calcular o valor da função f(x)
        def funcao(x):
            return a * x**9 + b * x**8 + c * x**7 + d * x**6 + e * x**5 + f * x**4 + g * x**3 + h * x**2 + i * x + j

        # Realiza o método de Bolzano
        resultado = ''
        if funcao(a_intervalo) * funcao(b_intervalo) < 0:
            # Encontra as raízes dentro do intervalo utilizando o método de Bolzano
            for x in range(int(a_intervalo), int(b_intervalo) + 1):
                if funcao(x) == 0:
                    raizes.append(x)

            if len(raizes) == 2:
                resultado = f'As duas raízes encontradas no intervalo [a, b] são: {raizes[0]} e {raizes[1]}'
            elif len(raizes) == 1:
                resultado = f'Há apenas uma raiz no intervalo [a, b], que é: {raizes[0]}'
            else:
                resultado = f'Há uma raiz no intervalo [a, b], mas não foi possível encontrá-la com precisão. Aproximação da raiz: {funcao((a_intervalo + b_intervalo) / 2)}'
        else:
            resultado = "Não há uma raiz no intervalo [a, b]."
    else:
        # Define o resultado como vazio caso não haja requisição POST
        resultado = ""

    return render(request, 'bolzano.html', {'resultado': resultado})






def met_bolzano(request):
    raizes = []

    if request.method == 'POST':
        # Obtém os valores do formulário e define 0 como valor padrão se estiverem vazios
        a = float(request.POST.get('a', 0)) if request.POST.get('a') else 0
        b = float(request.POST.get('b', 0)) if request.POST.get('b') else 0
        c = float(request.POST.get('c', 0)) if request.POST.get('c') else 0
        d = float(request.POST.get('d', 0)) if request.POST.get('d') else 0
        e = float(request.POST.get('e', 0)) if request.POST.get('e') else 0
        f = float(request.POST.get('f', 0)) if request.POST.get('f') else 0
        g = float(request.POST.get('g', 0)) if request.POST.get('g') else 0
        h = float(request.POST.get('h', 0)) if request.POST.get('h') else 0
        i = float(request.POST.get('i', 0)) if request.POST.get('i') else 0
        j = float(request.POST.get('j', 0)) if request.POST.get('j') else 0

        # Função para calcular o valor da função f(x)
        def calcular_funcao(x):
            return a + b * x + c * x**2 + d * x**3 + e * x**4 + f * x**5 + g * x**6 + h * x**7 + i * x**8 + j * x**9
        

        # Intervalo de x de -10 a 10
        funcao = np.arange(-10, 10)

        # Calcular os valores da função para cada x no intervalo
        resultados = []
        for x in funcao:
            resultado = calcular_funcao(x)
            resultados.append(resultado)  

        # Filtrar os pares de valores consecutivos que têm sinais diferentes
        pares_x_valores_filtrados = []
        for i in range(len(resultados)-1):
            if np.sign(resultados[i]) != np.sign(resultados[i+1]):
                par_x_valores_filtrados = (funcao[i], funcao[i+1])
                pares_x_valores_filtrados.append(par_x_valores_filtrados)

        # Passar os pares de valores de x filtrados para o template
        context = {
            'pares_x_valores_filtrados': pares_x_valores_filtrados
        }

        return render(request, 'bolzano.html', {'resultado': resultado})      




def filtrar_valores(request):
    # Função para calcular o valor da função para um dado x
    def calcular_funcao(x):
        if x >= 0:
            return 3 - 9*x + 1 * (3**x)
        else:
            return 3 - 9*x + 1 / (3**(-x))

    # Intervalo de x de -10 a 10
    x_valores = np.arange(-10, 11)

    # Calcular os valores da função para cada x no intervalo
    resultados = []
    for x in x_valores:
        resultado = calcular_funcao(x)
        resultados.append(resultado)

    # Filtrar os pares de valores consecutivos que têm sinais diferentes
    pares_x_valores_filtrados = []
    for i in range(len(resultados)-1):
        if np.sign(resultados[i]) != np.sign(resultados[i+1]):
            par_x_valores_filtrados = (x_valores[i], x_valores[i+1])
            pares_x_valores_filtrados.append(par_x_valores_filtrados)

    # Passar os pares de valores de x filtrados para o template
    context = {
        'pares_x_valores_filtrados': pares_x_valores_filtrados
    }

    return render(request, 'filtrar_valores.html', context)
