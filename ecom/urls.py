from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage, name="Home-Page"),
    path('shop/', all_prodyucsts, name="all_products" )
]