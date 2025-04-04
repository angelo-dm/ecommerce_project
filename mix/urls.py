from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('produto/<int:produto_id>/', views.details, name='details'),
]
