from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'POST':
    
    else:
        return render(request, 'index.html')
