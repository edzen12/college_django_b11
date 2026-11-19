from django.shortcuts import render
from apps.orientation.models import Orient


def homepage(request):
    orients = Orient.objects.select_related(
        'category'
    ).prefetch_related('tags')[:4]
    context = {
        'orients':orients,
    }

    return render(request, 'index.html', context)

# select_related - загружает связанную категорию вместе с направлением
# prefetch_related - заранее загружает теги
