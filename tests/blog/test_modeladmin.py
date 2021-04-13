from django.contrib.admin import ModelAdmin
from django.contrib.admin.sites import AdminSite
from django.test import TestCase, RequestFactory
import pytest

from blog.models import Post
from blog.admin import PostAdmin
from tests.account.factories import SuperUserFactory, GeneralUserFactory
from tests.blog.factories import PostFactory


class MockSuperUser:
    def has_perm(self, perm):
        return True


request_factory = RequestFactory()


class BasePostAdminTestCase:
    def setup_method(self, method):
        self.admin = PostAdmin(model=Post, admin_site=AdminSite())


class TestPostAdminBySuperUser(BasePostAdminTestCase):
    @pytest.mark.django_db
    def test_create_simple(self, auto_loggedin_superuser):
        client, user = auto_loggedin_superuser

        post = PostFactory()
        assert post.author is None

        request = request_factory.get('/admin/blog/post/add/')
        request.user = user
        self.admin.save_model(request, post, form=None, change=None)
        assert post.author == user

    @pytest.mark.django_db
    def test_change_by_owner(self, auto_loggedin_superuser):
        client, user = auto_loggedin_superuser

        post = PostFactory(author=user)
        assert post.author == user, 'save_model() の呼出し前は auhor が空であること'

        request = request_factory.get(f'/admin/blog/post/{post.id}/change')
        request.user = user
        post.body = 'updated!'
        self.admin.save_model(request, post, form=None, change=True)
        assert post.body == 'updated!'
        assert post.author == user, 'request ユーザが auhor となっていること'

    @pytest.mark.django_db
    def test_change_by_other_user(self, auto_loggedin_superuser):
        client, admin_user1 = auto_loggedin_superuser
        admin_user2 = SuperUserFactory(username='admin-user2')

        post = PostFactory(author=admin_user1)
        assert post.author == admin_user1

        request = request_factory.get(f'/admin/blog/post/{post.id}/change')
        request.user = admin_user2
        post.body = 'updated!'
        self.admin.save_model(request, post, form=None, change=True)
        assert post.body == 'updated!'
        assert post.author == admin_user1, '変更保存によって author は変更されないこと'


class TestPostAdminWithGeneralUser(BasePostAdminTestCase):
    @pytest.mark.django_db
    def test_create_simple(self, auto_loggedin_generaluser):
        client, user = auto_loggedin_generaluser

        request = request_factory.get('/admin/blog/post/add/')
        request.user = user

        post = PostFactory()
        assert post.author is None

        self.admin.save_model(request, post, form=None, change=None)
        assert post.author == user

    @pytest.mark.django_db
    def test_change_by_owner(self, auto_loggedin_generaluser):
        client, user = auto_loggedin_generaluser

        post = PostFactory(author=user)
        assert post.author == user, 'save_model() の呼出し前は auhor が空であること'

        request = request_factory.get(f'/admin/blog/post/{post.id}/change')
        request.user = user
        post.body = 'updated!'
        self.admin.save_model(request, post, form=None, change=True)
        assert post.body == 'updated!'
        assert post.author == user, 'request ユーザが auhor となっていること'

    @pytest.mark.django_db
    def test_change_by_other_user(self, auto_loggedin_generaluser):
        client, user1 = auto_loggedin_generaluser
        user2 = GeneralUserFactory(username='user2')

        post = PostFactory(author=user1)
        assert post.author == user1

        request = request_factory.get(f'/admin/blog/post/{post.id}/change')
        request.user = user2
        post.body = 'updated!'
        self.admin.save_model(request, post, form=None, change=True)
        assert post.body == 'updated!'
        assert post.author == user1, '変更保存によって author は変更されないこと'
