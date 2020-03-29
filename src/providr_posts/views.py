from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .forms import UserPostModelForm
from .models import UserPost
# Create your views here.

def user_post_list_view(request):
    #list objects/read objects
    qs = UserPost.objects.all()
    template_name = 'providr_posts/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

@login_required
def user_post_create_view(request):
    #create post
    form = UserPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = UserPostModelForm()
    template_name = 'form.html'
    context = {
        'form': form}
    return render(request, template_name, context)

def user_post_detail_view(request, slug):
    #read one object
    obj = get_object_or_404(UserPost, slug=slug)
    template_name = 'providr_posts/detail.html'
    context = {'object': obj}
    return render(request, template_name, context)

def user_post_update_view(request):
    obj = get_object_or_404(UserPost, slug=slug)
    template_name = 'providr_posts/update.html'
    context = {'object': obj, 'form': None}
    return render(request, template_name, context)

def user_post_delete_view(request):
    obj = get_object_or_404(UserPost, slug=slug)
    template_name = 'providr_posts/delete.html'
    context = {'object': obj}
    return render(request, template_name, context)
