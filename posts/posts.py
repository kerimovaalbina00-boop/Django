from posts.models import Post


def get_posts_filter_by_rate(rate):

    posts = Post.objects.filter(rate__gt=rate)

    return posts


def get_all_posts():
    posts = Post.objects.all()

    return posts