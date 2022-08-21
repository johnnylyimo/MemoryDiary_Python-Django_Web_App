from django.shortcuts import render, redirect


def home(request):
    if request.method == 'POST':
        newMemory = request.POST['memory']
        newMemory.save()
        return redirect('home')
    else:
        return render(request, 'index.html')
