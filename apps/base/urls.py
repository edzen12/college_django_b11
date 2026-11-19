from django.urls import path
from apps.base.views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
]