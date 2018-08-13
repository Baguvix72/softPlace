from django.shortcuts import render
from django.http import HttpResponse
from Post.models import Post, Category

def listPage(request):
    return HttpResponse("1\t2\n")
    #return render(request, 'Post/list.html')