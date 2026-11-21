from django.shortcuts import render, get_object_or_404
from apps.orientation.models import Orient


def orient_detail(request, slug):
    orient = get_object_or_404(Orient, slug=slug)
    context = {
        "orient":orient,
    }
    return render(request, 'pages/orientDetail.html', context)


def orient_page(request):
    orients = Orient.objects.all()
    context = {
        "orients":orients,
    }
    return render(request, 'pages/orients-page.html', context)