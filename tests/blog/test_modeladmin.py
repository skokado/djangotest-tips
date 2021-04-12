from django.contrib.admin import ModelAdmin
from django.contrib.admin.sites import AdminSite
from django.test import TestCase, RequestFactory
import pytest

from blog.models import Post
from blog.admin import PostAdmin
from tests.blog.factories import PostFactory


# @pytest.mark.django_db
# def test_create_post_as_adminuser(client, auto_loggedin_superuser):
#     post = PostFactory(
#         title='mypost1',
#         body='''
#             this is my first post.
#             Hi readers!
#         '''
#     )
#     assert post.author == auto_loggedin_superuser


class MockSuperUser:
    def has_perm(self, perm):
        return True


request_factory = RequestFactory()


class BasePostAdminTestCase:
    def setup_method(self, method):
        self.admin = PostAdmin(model=Post, admin_site=AdminSite())


class TestPostAdminWithSuperUser(BasePostAdminTestCase):

    @pytest.mark.django_db
    def test_create_post(self, auto_loggedin_superuser):
        client, user = auto_loggedin_superuser

        request = request_factory.get('/admin/blog/post/add/')
        request.user = user

        post = PostFactory()
        assert post.author is None

        self.admin.save_model(request, post, form=None, change=None)
        assert post.author == user

    @pytest.mark.django_db
    def test_change_post(self, auto_loggedin_superuser):
        client, user = auto_loggedin_superuser

        request = request_factory.get('/admin/blog/post/add/')
        request.user = user

        post = PostFactory(author=user)
        assert post.author == user
        
        post.body = 'updated!'
        self.admin.save_model(request, post, form=None, change=True)
        assert post.body == 'updated!'
        assert post.author == user


class TestPostAdminWithGeneralUser(BasePostAdminTestCase):
    @pytest.mark.django_db
    def test_create_by_generaluser(self, auto_loggedin_generaluser):
        client, user = auto_loggedin_generaluser

        request = request_factory.get('/admin/blog/post/add/')
        request.user = user

        post = PostFactory()
        assert post.author is None

        self.admin.save_model(request, post, form=None, change=None)
        assert post.author == user
