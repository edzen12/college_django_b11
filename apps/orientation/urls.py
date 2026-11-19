from django.urls import path
from apps.orientation.views import orient_detail

urlpatterns = [
    path('<slug:slug>/', orient_detail, name='orient_detail')
]