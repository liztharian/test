
from django.conf.urls import url,include
from . import views
from home.views import HomeView,CommentView,EditPost,DetailPost,view_post

urlpatterns=[


    url(r'^$',HomeView.as_view(),name='home'),
    #url(r'^comment/',CommentView.as_view(),name='comment')
    url(r'^comment/$',CommentView.as_view(),name='comment'),
    '''url(r'^view/',views.view_post,name='view_post'),
    url(r'^(?P<pk>\d+)$',DetailPost.as_view(),name='detail'),
    url(r'^(?P<pk>\d+)/edit$',EditPost.as_view(),name='edit'),'''


]
