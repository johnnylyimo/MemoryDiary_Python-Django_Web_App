from django.shortcuts import render, redirect
from . models import Memory

def home(request):
    if request.method == 'POST':
        newMemory = Memory(content=request.POST['memory'])
        newMemory.save()
        return redirect('home')
    else:
        return render(request, 'index.html')
