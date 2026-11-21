from django.urls import path
from apps.orientation.views import orient_detail, orient_page

urlpatterns = [
    path('', orient_page, name='orient_page'),
    path('<slug:slug>/', orient_detail, name='orient_detail'),

]