from . import views
from django.urls import path
from .views import (
    post_Vehicle_view,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostList,
    PostDetail,
    PostLike,
    post_Vehicle,
    delete_post,
    addVehicle,
    post_Vehicle_view
)

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('delete/<post_id>', delete_post, name='delete'),
    path('add_Vehicle/', addVehicle, name='add_Vehicle'),
    path('post_Vehicle/', post_Vehicle, name='post_Vehicle'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post_Vehicle_view/', post_Vehicle_view, name='post_Vehicle_view'),
    path('<slug:slug>/update', PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
