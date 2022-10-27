from article.models import Article
from article.serializers import ArticleListSerializer
from article.serializers import ArticleDetailSerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ArticleList(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)






class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
