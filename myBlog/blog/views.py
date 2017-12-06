from django.shortcuts import render
from django.http import Http404
from .forms import CommentForm
from .models import Blog
from .models import Comment
from .models import Category

def getMyHome(request):
    return render(request, 'myHome.html')


def getBlogList(request):
    ctx = {
        'blogs': Blog.objects.all().order_by('-created'),
        'blogs_category': '全部',
        'categorys': Category.objects.all()
    }
    return render(request, 'blogList.html', ctx)


def getBlogInCategory(request, category_id):
    categorys = Category.objects.filter(id=category_id)
    for category in categorys:
        category_name = str(category.name)
        print(category)
    ctx = {
        'blogs': Blog.objects.filter(category=categorys).order_by('-created'),
        'blogs_category': category_name,
        'categorys': Category.objects.all()
    }
    return render(request, 'blogList.html', ctx)


def getBlogDetail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)

    ctx = {
        'blog': blog,
        'categorys': Category.objects.all(),
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blogDetail.html', ctx)
