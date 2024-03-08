from django.urls import path
from recipes.views import home, second, third



urlpatterns = [
    path('', home),
    path('second/', second),
    path('third/', third),
]