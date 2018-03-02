from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.list_articles, name = 'list_articles'),
    url(r'^detail/(?P<pk>\d+)/$', views.detail_articles, name = 'detail_articles'),
    url(r'^create', views.create_articles, name = 'create_articles'),
    url(r'^edit/$', views.edit_articles, name = 'edit_articles'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit_this_article, name = 'edit_this_article'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete_article, name = 'delete_article'),
    url(r'^sign_up/$', views.sign_up, name = 'sign_up_article'),
    url(r'^login/$', views.login_user, name='login_user'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
]
