from django.shortcuts import render
from django.http import HttpResponse
from Post.models import Post, Category
from Post.otherCode import GetPagePost, GetIntCount, GetListPagin

def listPage(request, numPage, category):
    AllPost = Post.objects.all().order_by('-datePublic')
    AllCategory = Category.objects.all()

    PageCount = GetIntCount(AllPost.count(), 12)
    
    ListPagin = GetListPagin(PageCount, numPage)
    ListPosts = GetPagePost(AllPost, numPage)

    vars = {'ListPost':ListPosts, 'numPage':numPage, 'ListPagin':ListPagin, 'PageCount':PageCount, 'Category':AllCategory}
    return render(request, 'Post/list.html', vars)