
from rest_framework.generics import GenericAPIView
from kitaplar.models import Book,Comment
from kitaplar.api.serializers import BookSerializer,CommentSerializer
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from kitaplar.api.permission import IsAdminUserOrReadOnly ,IsCommentOwnOrReadOnly
from rest_framework.exceptions import ValidationError
from kitaplar.api.pagination import SmallPagination, LargePagination


class BookListCreateAPIView(generics.ListCreateAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   permission_classes = [IsAdminUserOrReadOnly]
   pagination_class = LargePagination

class BookDetailAPIView(generics.RetrieveAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   permission_classes = [IsAdminUserOrReadOnly]

class YorumCreateAPIView(generics.CreateAPIView):
   queryset = Comment.objects.all()
   serializer_class=CommentSerializer
   permission_classes = [IsAdminUserOrReadOnly]
   def perform_create(self, serializer):

      #  path('kitaplar/<int:kitap_pk>/yorum_yap/', api_views.YorumCreateAPIView.as_view(), name='kitap-yorumla'),
      book_pk = self.kwargs.get('book_pk')
      book = get_object_or_404(Book, pk=book_pk)
      user = self.request.user
      comment = Comment.objects.filter(book=book,comment_own=user)   # kullanıcının sadece bir yorum yapması gerekiyor diye yaptık
      if comment.exists():
         raise ValidationError('Bir kitaba sadece bir yorum yapabilirsiniz.')

      serializer.save(book=book,comment_own=user)

class CommentDetailAPIView(generics.RetrieveAPIView):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializer
   permission_classes = [IsCommentOwnOrReadOnly]



# class BookListCreateAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
#    def get(self,request, *args, **kwargs):
#       return self.list(request, *args, **kwargs)

#    def create(self,request, *args, **kwargs):
#       return self.list(request, *args, **kwargs)
