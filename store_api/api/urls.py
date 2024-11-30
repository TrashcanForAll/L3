from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
   path('get-token/', GetToken.as_view(), name='get_token'),
   path('get-goods/', GetGood.as_view(), name='get_goods'),
   path('new-good/', AddGoods.as_view()),
]