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
    resultados_bolzano = []
    resultados_bisseccao = []

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


        if all(val == 0 for val in [a, b, c, d, e, f, g, h, i, j, a_intervalo, b_intervalo]):
            return render(request, 'bolzano.html', {'resultado': [], 'resultado_biseccao': []})

        # Função para calcular o valor da função f(x)
        def calcular_funcao(x):
            return a + b * x + c * x**2 + d * x**3 + e * x**4 + f * x**5 + g * x**6 + h * x**7 + i * x**8 + j * x**9
        
        # Variável para armazenar o valor da função no início do intervalo
        f_a = calcular_funcao(a_intervalo)

        # Realiza o método de Bolzano

        for x in np.arange(a_intervalo + 1, b_intervalo + 1):
            f_x = calcular_funcao(x)
            if f_x == 0:
                resultados_bolzano.append(x)
            elif f_x * f_a < 0:
                resultados_bolzano.append((x - 1, x))
            f_a = f_x
        
        for intervalo in resultados_bolzano:
            if isinstance(intervalo, tuple):
                a, b = intervalo
                while abs(a - b) > 0.0001:  # critério de parada
                    c = (a + b) / 2
                    f_a = calcular_funcao(a)
                    f_c = calcular_funcao(c)
                    if f_c == 0:
                        resultados_bisseccao.append(c)
                        break
                    elif f_a * f_c < 0:
                        resultados_bisseccao.append((a, c))
                        b = c
                    else:
                        resultados_bisseccao.append((c, b))
                        a = c
            else:
                resultados_bisseccao.append(intervalo)
  
        
    return render(request, 'bolzano.html', {'resultado': resultados_bolzano, 'resultado_biseccao' : resultados_bisseccao})

    # Reinicializa as listas após a chamada do render
    resultados_bolzano = []
    resultados_bisseccao = []

def limpar_resultado(request):
    resultados_bisseccao = []
    resultados_bolzano = [] 
    

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
        def calcular_funcao(funcao):
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






def calcular(request):
    if request.method == 'POST':
        funcao = request.POST['funcao']  # Obtém a função inserida pelo usuário
        a = float(request.POST['a'])  # Obtém o valor inicial "a" fornecido pelo usuário
        b = float(request.POST['b'])  # Obtém o valor inicial "b" fornecido pelo usuário
        resultado = []  # Lista para armazenar os resultados da função

        # Cálculo da função usando o método de Bolzano
        while a <= b:
            x = (a + b) / 2  # Calcula o ponto médio do intervalo
            resultado.append({'valor': x, 'funcao': eval(funcao, {'x': x})})
            
            # Atualiza o intervalo "a" e "b" com base no valor da função no ponto médio
            if eval(funcao, {'x': a}) * eval(funcao, {'x': x}) < 0:
                b = x
            elif eval(funcao, {'x': b}) * eval(funcao, {'x': x}) < 0:
                a = x
            else:
                break  # Sai do loop se o valor da função for zero
            
        # Renderiza o resultado na página
        context = {'resultado': resultado}
        return render(request, 'calcular.html', context)
    
    # Se não houver uma solicitação POST, renderiza a página vazia
    return render(request, 'calcular.html')