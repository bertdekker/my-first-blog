from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    # Vul de variabele posts met een QuerySet:
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # Geef deze variabele als parameter door aan de render functie:
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
