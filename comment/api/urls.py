from django.urls import path, include
from comment.api.views.create_comment_view import CommentCreateAPIView
from comment.api.views.list_comment_view import CommentListAPIView
from comment.api.views.delete_comment_view import CommentDeleteAPIView
from comment.api.views.update_comment_view import CommentUpdateAPIView

app_name = "comment"
urlpatterns = [
    path('create', CommentCreateAPIView.as_view(), name='create'),
    path('list', CommentListAPIView.as_view(), name='list'),
    path('delete/<pk>', CommentDeleteAPIView.as_view(), name='delete'),
    path('update/<pk>', CommentUpdateAPIView.as_view(), name='update'),
]
