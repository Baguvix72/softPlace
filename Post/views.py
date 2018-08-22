from django.shortcuts import render, redirect
from django.http import HttpResponse
from Post.models import Post, Category
from Post.otherCode import GetPagePost, GetIntCount, GetListPagin, GetSpoiler

def homePage(request):
    return redirect(listPage, numPage = 1, category = "all")

def listPage(request, numPage, category):
    AllPost = Post.objects.all().order_by('-datePublic')
    AllCategory = Category.objects.all()

    if category != "all":
        CurrentCategory = AllCategory.get(urlName = category)
        AllPost = AllPost.filter(categorys = CurrentCategory)

    PageCount = GetIntCount(AllPost.count(), 12)
    
    ListPagin = GetListPagin(PageCount, numPage)
    ListPosts = GetPagePost(AllPost, numPage)

    vars = {'ListPost':ListPosts, 'numPage':numPage, 'ListPagin':ListPagin, 'PageCount':PageCount, 'SetCategory':AllCategory, 'ActiveCategory':category}
    return render(request, 'Post/list.html', vars)

def itemPage(request, numPost):
    CurrentPost = Post.objects.get(id = numPost)
    AllCategory = Category.objects.all()
    ListSpoilers = GetSpoiler(CurrentPost.collap)

    vars = {'SetCategory':AllCategory, 'Post':CurrentPost, 'Spoilers':ListSpoilers}
    return render(request, 'Post/item.html', vars)