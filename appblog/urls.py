from django.urls import path
from .views import AddCategoryPost, DeletePost, Homeview, BlogDetailview, AddPost, UpdatePost, CategoryView, CategoryListView, LikeView, AddCommentView, search_bar, Aboutpage

urlpatterns = [
    #path('', views.home, name='home'),
    path('', Homeview.as_view(), name='home'),
    path('blog/<int:pk>', BlogDetailview.as_view(), name='blog-detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('post/edit/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('post/<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
    path('add_category/', AddCategoryPost.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name = 'category'),
    path('category_list/', CategoryListView, name = 'category-list'),
    path('like/<int:pk>', LikeView, name = 'like-post'),
    path('blog/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('search_bar/', search_bar.as_view(), name='search_bar'),
    path('about/', Aboutpage, name='about_page'),
    
]
