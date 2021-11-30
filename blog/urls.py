from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^rozklad$', views.google_rozklad, name='google_rozklad'),
    url(r'^predmets$', views.predmets, name='predmets'),
    url(r'^news$', views.news, name='news'),
    url(r'', views.home, name='home'),
    url(r'^predmets/marks/$', views.marks, name='marks'),
    url(r'^predmets/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail')
]