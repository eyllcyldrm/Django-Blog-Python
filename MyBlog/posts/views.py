from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.
def index(request):
    return HttpResponse('Merhaba Dünya')

def post_create(request):
    return HttpResponse('Post Oluşturuluyor')

def post_detail(request):
    return HttpResponse('Post Detayı')

def post_update(request):
    return HttpResponse('Post Güncelleniyor Path')

def post_list(request):
    #return HttpResponse("Şu anda listeleniyor.")
    post_list=Post.objects.all()
    return render(request,'posts/post_list.html',context={'post_list':post_list})
