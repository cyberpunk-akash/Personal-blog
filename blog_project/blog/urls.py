from django.conf.urls import url
from blog import views
from django.urls import path

urlpatterns=[
url(r'^about/$',views.AboutView.as_view(),name='about'),
url(r'^$',views.PostListView.as_view(),name='post_list'),
path('<int:pk>/',views.PostDetailedView.as_view(),name='post_detail'),
url(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
path('post/<int:pk>/edit/',views.PostUpdateView.as_view(),name='post_edit'),
path('post/<int:pk>/remove/',views.PostDeleteView.as_view(),name='post_remove'),
path('draft/',views.DraftListView.as_view(),name='post_draft_list'),
path('post/<int:pk>/comment/',views.add_comments_to_post,name='add_comment_to_post'),
path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
path('<int:pk>/publish/',views.post_publish, name='post_publish')
]
