from .models import Svaz
from django.shortcuts import render, get_object_or_404


def test1(request):
    return render(request, 'main/html/test.html', {'video_list': Svaz.objects.order_by('-data_roj')})


