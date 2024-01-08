from django.urls import path, include
from post_data.api.views.post_list import PostList

urlpatterns = [
    path('list', PostList.as_view(), name='list')
]
