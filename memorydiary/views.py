from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        newMemory = request.POST['memory']
        newMemory.save()
    else:
        return render(request, 'index.html')
