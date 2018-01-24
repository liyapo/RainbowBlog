from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_articles, name = 'list_articles'),
    url(r'^detail/(?P<pk>\d+)/$', views.detail_articles, name = 'detail_articles'),
    url(r'^create', views.create_articles, name = 'create_articles'),
    url(r'^edit/$', views.edit_articles, name = 'edit_articles'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit_this_article, name = 'edit_this_article'),
]
