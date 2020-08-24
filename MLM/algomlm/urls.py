from django.urls import path
from algomlm import views

urlpatterns = [
    path('',views.base,name='base'),
]