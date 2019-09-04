from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
    # 글 목록이 있는 posts 변수를 템플릿에 넘기기
    # 이 후 템플릿이 posts 변수를 받아 HTML에 나타냄 (파이썬을 html로 변경해줌)
