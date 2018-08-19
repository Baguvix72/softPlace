from django.shortcuts import render
from django.http import HttpResponse
from Post.models import Post, Category
from Post.otherCode import GetPagePost, GetIntCount, GetListPagin

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

def itemPage(request):
    AllCategory = Category.objects.all()
    vars = {'SetCategory':AllCategory}
    return render(request, 'Post/item.html', vars)