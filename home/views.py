from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404


def login(request):
    pass

def index(request):
    pass


class CreatePost(APIView):
    def post(self, request, format=None):
        serializer = PostDeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()[0:5]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostDetail(APIView):
    def get_object(self, post_id):
        try:
            return Post.objects.get(post_id=post_id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, post_id, format=None):
        product = self.get_object(post_id)
        PostSerializer(product)
        return Response(serializer.data)

class AuthorList(APIView):
    pass
