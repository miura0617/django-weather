from django.urls import path, include
from .views import TopView, WeatherAPIView

urlpatterns = [
    path('top/', TopView.as_view()),    # クラスベースビュー
    path('api/<int:pk>/', WeatherAPIView.as_view())
]
