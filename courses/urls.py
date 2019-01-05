from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostUpdateView, PostDeleteView, PostCreateView, UserPostListView


urlpatterns = [
    path('home/', PostListView.as_view(), name='courses-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name='courses-about'),
    path('', views.first, name='courses-first'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('myclasses/', views.myclasses,name='myclasses'),
]