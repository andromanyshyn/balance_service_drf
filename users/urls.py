from django.urls import path
from . import views

urlpatterns = [
    path('balance/add/', views.UserBalanceAdd.as_view(), name='balance_add'),
    path('balance/subtract/', views.UserBalanceSubtract.as_view(), name='balance_subtract'),
    path('balance/send/', views.UserBalanceSend.as_view(), name='balance_send'),
    path('balance/check/<int:pk>/', views.UserBalanceCheck.as_view(), name='balance_check'),
]