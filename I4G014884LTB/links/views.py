from django.shortcuts import render
from django.views import generic        #importing generic class so we can use the ListView method.
from .models import Link
from .serizliers import LinkSerializer

# Create your views here.
class PostListApi(generic.ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(generic.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailApi(generic.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi(generic.UpdateAPIView):
    queryset = Link.object.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi(generic.DestroyAPIView):
    queryset= Link.objects.filter(active=True)
    serializer_class = LinkSerializer

