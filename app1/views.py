from django.shortcuts import render

# Create your views here.
def nanda(request):
    return render(request,'nanda.html')

def contact(request):
    return render(request,'contact.html')