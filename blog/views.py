from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    context = {'posts': posts}
    return render(request, 'index.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'post_detail.html', context)