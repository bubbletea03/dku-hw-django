from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('portfolio/', include('PortfolioApp.urls')),
    path('admin/', admin.site.urls),
]
