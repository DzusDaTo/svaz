from django.shortcuts import render, redirect
from .forms import *


def svaz(request):
    if request.method == 'POST':
        form = SvazForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = SvazForm()
    return render(request, 'news/html/svaz.html', {'form': form})
