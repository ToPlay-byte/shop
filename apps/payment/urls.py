from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('ajax/cities/', views.AjaxCitiesView.as_view()),
    path('ajax/delete-order', views.AjaxDeleteOrderView.as_view()),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('<str:pk>', views.OrderView.as_view(), name='order'),
    path('my-orders/', views.OrdersList.as_view(), name='orders-list'),
]