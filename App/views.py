from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from App.models import Category, Post, Comment, ReplyComment
from .forms import CommentForm, ReplyForm
from .filters import TitleFilter
import random

def Home(request): 
    try:
        top_post = Post.objects.filter(recommended=True).order_by('-created_on')
        top_post = top_post[:2]
    except:
        pass

    post = Post.objects.all().order_by('-created_on')
    
    # Get Most Read Posts
    views = []
    most_read = ''
    try:
        for pos in post:
            views.append(pos.views)
        views.sort()
        most_read = Post.objects.filter(views__gte=views[-3])  #Use views gt views[-3]   instead 
    except:
        pass

    # Get the number of post for each category
    category = Category.objects.all()
    h = []
    for i in category:
        f = Post.objects.filter(categories__name__contains=i)
        k = str(i)
        h.append({k:f.count()})
    
    #Feature Post: Gotten randomly
    feature = ''
    try:
        i = random.randint(1,category.count())
        j = Category.objects.get(id=i)
        feature = Post.objects.filter(categories__name__contains=j)
        try:
            feature = feature[:3]
        except:
            pass
    except:
        pass
    
    search = TitleFilter(request.GET, queryset=post)
    post = search.qs
    if post:
        post = post[:6]

    context = {
        'top_post': top_post,
        'post': post,
        'most_read': most_read,
        'category': category,
        'search': search,
        'h': h,
    }
    html=['App/index.html','base.html']
    return render(request,html, context)

def Categories(request,category):
    try:
        top_post = Post.objects.filter(recommended=True).order_by('-created_on')
        top_post = top_post[:2]
    except:
        pass

    post = Post.objects.all().order_by('-created_on')
    posts = Post.objects.filter(categories__name__contains = category).order_by('-created_on')
    if posts.count() < 1:
        messages.error(request,'No Post Available yet for this Category {category}')
        
    
    # Get Most Read Posts
    views = []
    try:
        for pos in post:
            views.append(pos.views)
        views.sort()
        most_read = Post.objects.filter(views__gte=views[-3])
    except:
        pass
    #End

    #Get Recent Post
    search = TitleFilter(request.GET, queryset=post)
    post = search.qs
    if post:
        post = post[:6]

    cat = category
    # Get the number of post for each category
    category = Category.objects.all()
    h = []
    for i in category:
        f = Post.objects.filter(categories__name__contains=i)
        k = str(i)
        h.append({k:f.count()})
    #End
    
    search = TitleFilter(request.GET, queryset=posts)
    posts = search.qs[:6]
    if posts:
        posts = posts[:6]

    context = {
        'top_post': top_post,
        'cat': cat,
        'post': post,
        'posts': posts,
        'category': category,
        'most_read': most_read,
        'search': search,
        'h': h,
    }
    html=['App/category.html','base.html']
    return render(request,html,context)


def Detail(request,category,slug):
    post = Post.objects.all().order_by('-created_on')
    detail_post = Post.objects.get(slug=slug)
    
    # Get Most Read Posts
    views = []
    most_read = ''
    try:
        for pos in post:
            views.append(pos.views)
        views.sort()
        most_read = Post.objects.filter(views__gte=views[-3])  #Use views gt views[-3]   instead 
    except:
        pass
    #End

    # Get the number of post for each category
    category = Category.objects.all()
    h = []
    for i in category:
        f = Post.objects.filter(categories__name__contains=i)
        k = str(i)
        h.append({k:f.count()})
    #End

    #Get Featured post 
    feature = ''
    try:
        i = random.randint(1,category.count())
        j = Category.objects.get(id=i)
        feature = Post.objects.filter(categories__name__contains=j)
        try:
            feature = feature[:3]
        except:
            pass
    except:
        pass
    #End
    
    if request.method == 'GET':
        detail_post.views = detail_post.views + 1
        detail_post.save()


    #_______________Forms___________________
    # Comment Form
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']

            Comment.objects.create(
                name = name,
                email = email,
                message = message,
                post = detail_post
            )

    messages.success(request, 'Message sent successfull!!!')
    #End
    comment = Comment.objects.filter(post=detail_post).order_by('-created_on')
    context = {
        'post': post,
        'detail_post': detail_post,
        'category': category,
        'most_read': most_read,
        'feature': feature,
        'h': h,
        'form': form,
    }
    html=['App/detail.html','base.html']
    return render(request,html,context)

def GetComment(request,id):
    post = Post.objects.get(id=id)
    comment = Comment.objects.filter(post=post)
    return JsonResponse({"comment": list(comment.values())})
    # return JsonResponse('working', safe=False)

def getReplies(request, id):
    reply = ReplyComment.objects.filter(comment=id)
    return JsonResponse({"reply": list(reply.values())})

def Reply(request,category,slug,comment_id):

    post = Post.objects.all().order_by('-created_on')
    category = Category.objects.all()

    comment = Comment.objects.get(id=comment_id)
    
    # Reply Form
    reply_form = ReplyForm()
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        ReplyComment.objects.create(
            name = name,
            email = email,
            message = message,
            comment = comment
        )

    messages.success(request, 'Message sent successfull!!!')

    reply = ReplyComment.objects.filter(comment=comment).order_by('-created_on')

    context = {
        'post': post,
        'category': category,
        'comment': comment,
        'reply_form': reply_form,
        'reply': reply,
    }
    html=['App/reply.html','base.html']
    return render(request,html,context)

def About(request):
    post = Post.objects.all().order_by('-created_on')

    #Get Recent Post
    search = TitleFilter(request.GET, queryset=post)
    post = search.qs
    if post:
        post = post[:6]
    
    # Get Most Read Posts
    views = []
    most_read = ''
    try:
        for pos in post:
            views.append(pos.views)
        views.sort()
        most_read = Post.objects.filter(views__gte=views[-3])  #Use views gt views[-3]   instead 
    except:
        pass
    #End

    # Get the number of post for each category
    category = Category.objects.all()
    h = []
    for i in category:
        f = Post.objects.filter(categories__name__contains=i)
        k = str(i)
        h.append({k:f.count()})
    #End

    context = {
        'post': post,
        'most_read': most_read,
        'h': h,
        'category': category,
    }
    html=['App/about.html','base.html']
    return render(request,html,context)

def Contact(request):
    post = Post.objects.all().order_by('-created_on')
    category = Category.objects.all()

    #Get Recent Post
    search = TitleFilter(request.GET, queryset=post)
    post = search.qs
    if post:
        post = post[:6]

    context = {
        'post': post,
        'category': category,
    }
    html=['App/contact.html','base.html']
    return render(request,html,context)
    