from .views import Registration_view
from django.urls import path

urlpatterns = [
    path('register/', Registration_view.as_view(), name='register'),
]