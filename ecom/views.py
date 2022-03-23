from django.shortcuts import render

# Create your views here.

def HomePage(request):
    return render(request, 'front/index.html')



def all_prodyucsts(request):
    return render(request, 'front/shop.html')