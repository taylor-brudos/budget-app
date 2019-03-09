from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^myaccounts$', views.myaccounts),
    url(r'^accountdetail$', views.show),
]