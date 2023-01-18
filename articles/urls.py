from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('create', views.article_create, name='create'),
    path('<slug:slug>/', views.article_detail, name='detail'),
    path('<slug:slug>/comment', views.AddCommentView.as_view(), name='add_comment'),
    path('<slug:slug>/like', views.LikeView, name='like_post'),
]