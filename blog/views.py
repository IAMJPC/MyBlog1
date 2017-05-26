from django.shortcuts import render
from blog.models import *
from blog.CommentForms import CommentForm
from django.http import Http404

# Create your views here.


def get_blogs(request):
    get_blogs_ctx = {'blog': Blog.objects.all().order_by('blogReleasedTime')}
    return render(request, 'blog_list.html', get_blogs_ctx)


def get_details(request, blog_id):
    try:
        blogs = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blogs
            Comment.objects.create(**cleaned_data)
    get_details_ctx = {
        'blog': blogs,
        'comments': blogs.comment_set.all().order_by('commentReleasedTime'),
        'form': form
    }
    return render(request, 'blog_detail.html', get_details_ctx)