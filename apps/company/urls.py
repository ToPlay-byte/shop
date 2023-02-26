from django.urls import path
from apps.company import views

app_name = 'company'

urlpatterns = [
    path('', views.HomeView.as_view(), name='Home')
]