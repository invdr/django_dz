from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='article_list'),
    # path('contacts/', get_contacts, name='contacts'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('article/<int:pk>/', BlogDetailView.as_view(), name='article'),
    path('update/<int:pk>/', BlogDetailView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDetailView.as_view(), name='delete'),

]
