from django.urls import path, include
from post_data.api.views.post_list_view import PostListAPIView
from post_data.api.views.post_detail_view import PostDetailAPIView
from post_data.api.views.post_delete_view import PostDeleteAPIView
from post_data.api.views.post_update_view import PostUpdateAPIView
from post_data.api.views.post_create_view import PostCreateAPIView


app_name = "post"
urlpatterns = [
    path('list', PostListAPIView.as_view(), name='list'),
    path('detail/<slug>', PostDetailAPIView.as_view(), name='detail'),
    path('delete/<slug>', PostDeleteAPIView.as_view(), name='delete'),
    path('update/<slug>', PostUpdateAPIView.as_view(), name='update'),
    path('create', PostCreateAPIView.as_view(), name='create'),
]
