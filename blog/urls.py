from django.urls import path
from . import views
from .views import(
     PostListView,
     PostDetailView,
     PostCreateView,
     PostUpdateView,
     PostDeleteView,
     UserPostListView,CategoryPostListView
)


urlpatterns = [
    path('',PostListView.as_view(),name= 'blog home'),
    path('user/<str:username>',UserPostListView.as_view(),name= 'user posts'),
    path('category_posts/<str:category>',CategoryPostListView.as_view(),name= 'category-posts'),
    path('about/',views.about,name= 'blog about'), 
    path('contact/',views.contact,name= 'blog contact'), 
    path('blogpost/<int:pk>',PostDetailView.as_view(),name= 'blog post'),
    path('create/',PostCreateView.as_view(),name= 'post create'),
    path('blogpost/<int:pk>/update/',PostUpdateView.as_view(),name= 'post update'),
    path('blogpost/<int:pk>/delete/',PostDeleteView.as_view(),name= 'post delete'),
]