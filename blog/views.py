from django.shortcuts import render, HttpResponse, redirect
from blog.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from blog.templatetags import extras
import math

# Create your views here.
def blog(request):
    page = request.GET.get('page')
    no_of_post = 3
    if page is None:
        page = 1
    else:
        page = int(page)

    if request.method == 'POST':
        s_category = request.POST['category']

        if s_category == '':
            messages.error(request, 'Please enter a category not a choose')
            return render(request, 'blog/blog.html')

        else:
            search = Post.objects.filter(category=s_category)
            context = {'allPost': search}
            return render(request, 'blog/blog.html', context)
    else:
        allPost = Post.objects.all()
        length = len(allPost)
        allPost = allPost[(page-1)*no_of_post: page*no_of_post]
        if page > 1:
            prev = page -1
        else:
            prev=None

        if page<math.ceil(length/no_of_post):
            nxt = page + 1

        else:
            nxt = None
        context = {'allPost': allPost, 'prev': prev, 'next': nxt}
        return render(request, 'blog/blog.html', context)

def blogpost(request, slug):
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    # i will increase views of blogpost
    post.views += 1
    post.save()
    return render(request, 'blog/blogpost.html', context)

def create_post(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        slug = request.POST['slug']
        category = request.POST['category']
        contant = request.POST['id_contant']

        post = Post(title=title, author=author, slug=slug, views=0, category=category, content=contant)
        post.save()
        messages.success(request, "Your post has been created successfully")
    return render(request, 'blog/create_post.html')

def search_post(request):
     if request.method == 'POST':
        s_category = request.POST['category']

        if s_category == '':
            messages.error(request, 'Please enter a category not a choose')
            return render(request, 'blog/search_c.html')
        
        else:
            search = Post.objects.filter(category=s_category)
            context = {'allPost': search}
            return render(request, 'blog/search_c.html', context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        comment=BlogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")
