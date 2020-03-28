from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import UserPost
# Create your views here.

def user_post_list_view(request):
    #list objects/read objects
    qs = UserPost.objects.all()
    template_name = 'user_post_list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

def user_post_create_view(request):
    #create post
    template_name = 'user_post_create.html'
    context = {'form': None}
    return render(request, template_name, context)

def user_post_detail_view(request, slug):
    #read one object
    obj = get_object_or_404(UserPost, slug=slug)
    template_name = 'user_post_detail.html'
    context = {'object': obj}
    return render(request, template_name, context)

def user_post_update_view(request):
    obj = get_object_or_404(UserPost, slug=slug)
    template_name = 'user_post_update.html'
    context = {'object': obj, 'form': None}
    return render(request, template_name, context)

def user_post_delete_view(request):
    obj = get_object_or_404(UserPost, slug=slug)
    template_name = 'user_post_delete.html'
    context = {'object': obj}
    return render(request, template_name, context)
