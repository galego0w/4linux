from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

def post_list(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(data_criado__lte=timezone.now()).order_by('data_criado')
    return render(request,'blog/post_list.html',{'posts':posts})


def post_detail(request, pk):
    # post = get_object_or_404(Post,pk=pk)
    post = Post.objects.get(pk)
    return render(request,'blog/post_detail.html/',{'post':post})
