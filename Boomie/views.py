from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Boomie.models import Category, Post, Comment, ReplyComment
from .forms import CommentForm, ReplyForm
from .filters import TitleFilter
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url = 'login')
def index(request):
    post = Post.objects.all()
    # .order_by('-created_on')
    
    search = TitleFilter(request.GET, queryset=post)
    post = search.qs
    context = {
        'post': post,
        'search': search,
    }
    return render(request,'boomie/11.html', context)

@login_required(login_url = 'login')
def detail(request, slug, category):
    post = Post.objects.get(slug=slug)
    
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                body = form.cleaned_data['body'],
                user = request.user, #This gets the recent logged in user and saves it to the database with the comment.
                post = post
            )
            comment.save()
    
    comment = Comment.objects.filter(post=post)
    
    post.views += 1
    post.save()

    context = {
        'post': post,
        'form': form,
        'comment': comment,
    }
    return render(request, 'boomie/22.html', context)

def reply(request, slug, category, id):
    post = Post.objects.get(slug=slug)
    comment = Comment.objects.filter(post=post)
    comment_id = Comment.objects.get(id=id)

    form = ReplyForm()
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = ReplyComment(
                body = form.cleaned_data['body'],
                user = request.user, #This gets the recent logged in user and saves it to the database with the comment.
                comment = comment_id
            )
            reply.save()
    reply = ReplyComment.objects.filter(comment=comment_id)

    context = {
        'post': post,
        'form': form,
        'reply': reply,
        'comment_id': comment_id,
    }

    return render(request, 'boomie/comment.html', context)

@login_required(login_url = 'login')
def category(request, category):
    posts = Post.objects.all()
    post = Post.objects.filter(categories__name__contains= category).order_by('-created_on')

    search = TitleFilter(request.GET, queryset=post)
    post = search.qs

    context = {
        'post': post,
        'posts': posts,
        'search': search,
        'category': category,
    }
    return render(request, 'boomie/33.html', context)
