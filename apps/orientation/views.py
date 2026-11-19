from django.shortcuts import render, get_object_or_404
from apps.orientation.models import Orient


def orient_detail(request, slug):
    orient = get_object_or_404(Orient, slug=slug)
    context = {
        "orient":orient,
    }
    return render(request, 'orientDetail.html', context)