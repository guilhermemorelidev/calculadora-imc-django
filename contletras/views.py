from django.shortcuts import render

def contar_letras(request):
    texto = ''
    resultado = None

    if request.method == 'POST':
        texto = request.POST.get('texto', '')
        contagem = len(texto)

        resultado = {
            'letras': contagem
        }

    return render(request, 'contletras/formulario.html', {
        'texto': texto,
        'resultado': resultado
    })