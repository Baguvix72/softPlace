from django.shortcuts import render
from django.http import HttpResponse
from Post.models import Post, Category
from Post.otherCode import GetListPosts, GetIntCount

def listPage(request, numPage):
    AllPost = Post.objects.all().order_by('-datePublic')
    AllCategory = Category.objects.all()

    PageCount = GetIntCount(AllPost.count(), 12)

    PostsPage = AllPost[numPage * 12 - 12:numPage * 12]
    ListPosts = GetListPosts(PostsPage)

    vars = {'ListPost':ListPosts, }
    return render(request, 'Post/list.html', vars)