from django.shortcuts import render
from .services import get_blog, get_comments,get_comments, info_blog, get_category, last_commet
from .forms import BlogModelForm,Comment
from .models import Blog,Comments
from django.contrib.auth.models import User

# Create your views here.

def blog(request):
    blog = get_blog()
    categorys = get_category()
    last_commets = last_commet()
    ctx = {
        'blogs': blog,
        'categorys': categorys,
        'last_commets':last_commets
    }
    return render(request, 'blog/blog.html', ctx)


def add_post(request):
    form = BlogModelForm()
    contex ={
        'form':form
    }
    return  render(request, 'blog/post.html', contex)


def add_db(request):
    if request.POST:
        form = BlogModelForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
    ctx = {
        'form':form
    }
    return render(request, 'blog/post.html',ctx)


def search(request):
    if request.POST:
        query = request.POST["s"]
        queryset = Blog.objects.filter(name__contains=query)
    else:
        queryset = "PLease enter blog name !!!"
    contex ={
        'query':query,
        'queryset':queryset
    }
    return render(request, 'blog/search.html', contex)

def blog_detail(request, id):
    if request.POST:
        print(request.POST)
        comment = Comments()
        comment.message = request.POST.get("message")
        user_instance = User.objects.get(id=request.POST.get("user_id"))
        blog_instance = Blog.objects.get(id=request.POST.get("blog_id"))
        comment.blog = blog_instance
        comment.user = user_instance
        comment.save()
        success = f'{request.POST.get("message")}'
        return HttpResponse(success)


    blog = info_blog(id)
    comments = get_comments(id)
    user_id = request.user.id
    forms = Comment()
    contex = {
        'blog': blog,
        'comments': comments,
        'forms': forms,
        "user_id" : user_id
    }
    return render(request, 'blog/single-post.html', contex)