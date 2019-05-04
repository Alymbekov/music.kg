from django.urls import path
from musickg.views import index

urlpatterns = [
    path('', index, name="index")
]
