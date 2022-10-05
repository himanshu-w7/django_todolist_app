from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='task'),
    # path('', views.index, name='addingRecord'),
]
