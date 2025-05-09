from django.urls import path
from . import views

app_name = 'PortfolioApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:project_id>/', views.detail, name='detail'),
    path('<int:project_id>/rate', views.rate, name='rate'),
]