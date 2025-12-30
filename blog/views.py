from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def main_page(request):
    return render(request, 'blog/blog_main.html', )
