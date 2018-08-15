from django.shortcuts import render
from django.http import HttpResponse
from Post.models import Post, Category
from Post.otherCode import GetPostList

def listPage(request):
    AllPost = Post.objects.all().order_by('-datePublic')
    AllCategory = Category.objects.all()

    PostsFirsts_12 = AllPost[0:12]

    ListPost = GetPostList(PostsFirsts_12)

    vars = {'Posts': PostsFirsts_12, 'AllCategory': AllCategory, 'ListPost':ListPost, }
    return render(request, 'Post/list.html', vars)