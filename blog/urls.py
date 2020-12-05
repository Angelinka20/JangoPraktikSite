from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^rozklad$', views.google_rozklad, name='google_rozklad'),
]