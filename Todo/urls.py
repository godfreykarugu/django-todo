from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<id>', views.delete, name='delete'),
    path('update/<id>', views.update, name='update'),
    path('view/<id>', views.view, name='view')

]