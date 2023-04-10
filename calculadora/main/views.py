import numpy as np
from django.shortcuts import render

# Create your views here.


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

    
