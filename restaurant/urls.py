from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.board_list_hall, name='board_list_hall'),
    url(r'^order$', views.order, name='order'),
]