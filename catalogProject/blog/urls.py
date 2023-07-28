from django.urls import path, re_path
from .feeds import LatestPostsFeed
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('tag/<tag_slug>/', views.post_list, name='post_list_by_tag'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/(?P<post>[-\w]+)/$', views.post_detail,
            name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]
