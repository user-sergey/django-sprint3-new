from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render

from blog.models import Category, Post

NUMBER_OF_POSTS = 5


def index(request):
    context = {
        'post_list': Post.get_published()[:NUMBER_OF_POSTS],
    }
    template_name = 'blog/index.html'
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(Post.get_published(), id=id)
    try:
        context = {
            'post': post,
        }
        return render(request, template_name, context)
    except IndexError:
        return HttpResponseNotFound('<h1>404 Not Found</h1>')


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(is_published__exact=True),
        slug=category_slug
    )
    context = {
        'post_list': Post.get_published().filter(category=category),
        'category': category,
    }
    return render(request, template_name, context)
