from django.urls import path

from tours import views


urlpatterns = [
    path('', views.index),
    path('departure/<str:departure>/', views.departure),
    path('tour/<int:tour_id>/', views.tour),
]
