from django.urls import path
from .views import like_change

app_name = "like"

urlpatterns = [
    path('like_change', like_change, name='like_change'),
]