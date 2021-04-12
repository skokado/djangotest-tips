from factory.django import DjangoModelFactory

from blog.models import Post


class PostFactory(DjangoModelFactory):
    title = 'post1'
    body = '''
        this is my first post.
        Hi readers!
    '''.strip()

    class Meta:
        model = Post
