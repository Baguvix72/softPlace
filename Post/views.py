from django.shortcuts import render
from django.http import HttpResponse
from Post.models import Post, Category

def listPage(request):
    AllPost = Post.objects.all().order_by('-datePublic')
    AllCategory = Category.objects.all()

    PostsFirsts_12 = AllPost[0:12]
    PostCount = PostsFirsts_12.count()

    FirstGrup = AllPost[0:3]
    SecondGrup = AllPost[3:6]
    ThriedGrup = AllPost[6:9]
    FourGrup = AllPost[9:12]

    ListPost = [FirstGrup, SecondGrup, ThriedGrup, FourGrup]

    vars = {'Posts': PostsFirsts_12, 'AllCategory': AllCategory, 'ListPost':ListPost}
    return render(request, 'Post/list.html', vars)

    #def GetRowCount(self, PostCount):
