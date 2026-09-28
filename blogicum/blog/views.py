from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post

NUMBER_OF_POSTS = 5


def get_published_posts(posts=None):
    if posts is None:
        posts = Post.objects.all()

    return posts.filter(
        is_published__exact=True,
        category__is_published__exact=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    return render(
        request,
        'blog/index.html',
        {'post_list': get_published_posts()[:NUMBER_OF_POSTS]}
    )


def post_detail(request, post_id):
    post = get_object_or_404(get_published_posts(), id=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        is_published__exact=True,
        slug=category_slug
    )
    posts_of_category = category.posts.all()
    published_posts = get_published_posts(posts=posts_of_category)
    return render(
        request,
        'blog/category.html',
        {'post_list': published_posts, 'category': category}
    )
