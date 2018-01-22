from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_articles, name = 'list_articles'),
    url(r'^$', views.detail_articles, name = 'detail_articles'),
    url(r'^$', views.create_articles, name = 'create_articles'),
    url(r'^$', views.edit_articles, name = 'edit_articles'),
]
