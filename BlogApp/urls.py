from django.urls import path
from BlogApp import views
from .views import HomeView, ArticleDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    #path('admin/', views.urls),
    path('', HomeView.as_view(), name="Home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"), #pk parametro.
    path('add_post/', PostCreateView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', PostUpdateView.as_view(), name="update_post"),
    path('article/delete/<int:pk>', PostDeleteView.as_view(), name="delete_post"),
]
