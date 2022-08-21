from django.shortcuts import render, redirect
from . models import Memory

def home(request):
    if request.method == 'POST':
        newMemory = Memory(content=request.POST['memory'])
        newMemory.save()

    else:
        return render(request, 'index.html')
