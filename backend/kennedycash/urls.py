from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListPersonalTransaction.as_view()),
    path('<int:pk>/', views.DetailPersonalTransaction.as_view()),
]
