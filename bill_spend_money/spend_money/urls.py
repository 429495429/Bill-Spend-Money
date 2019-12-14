from django.urls import path
from . import views
app_name = 'spend_moeny'
urlpatterns = [
    path('', views.index, name='index'),
    
]