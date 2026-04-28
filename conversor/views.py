from django.shortcuts import render

# Create your views here.
def converter_dinheiro(request):
    if request.method == 'POST':
        valor_reais = float(request.POST.get('valor_reais', 0))
        valor_dolar = valor_reais / 5.0  # Supondo uma taxa de câmbio fixa
        return render(request, 'conversor/index.html', {'valor_dolar': valor_dolar})
    
    return render(request, 'conversor/index.html')
    
  