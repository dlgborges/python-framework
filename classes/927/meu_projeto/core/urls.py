from django.urls import path
from .views import home
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('criar/', criar, name='criar'),
    path('editar/<int:id>/', editar, name='editar'),
    path('deletar/<int:id>/', deletar, name='deletar')
]
