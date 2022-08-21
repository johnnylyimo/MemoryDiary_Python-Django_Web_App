from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if request.method == 'POST':
    
    else:
        return render(request, 'index.html')
