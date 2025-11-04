from django.urls import path
from .views import predict_survival

urlpatterns = [
    path('api/predict/', predict_survival, name='predict_survival'),
]
