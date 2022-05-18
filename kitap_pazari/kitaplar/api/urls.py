
from unicodedata import name
from django.urls import path
from . import views as api_views

urlpatterns = [
   path('books/',api_views.BookListCreateAPIView.as_view(),name='book-list'),
   path('books/<int:pk>',api_views.BookDetailAPIView.as_view(),name='book-detail'),
   path('books/<int:book_pk>/to_comment', api_views.YorumCreateAPIView.as_view(), name='to-comment'),
   path('comments/<int:pk>',api_views.CommentDetailAPIView.as_view(), name='commnets'),
]