from django.http.response import Http404
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse, resolve
from django.test import RequestFactory
from mixer.backend.django import mixer
import pytest

from account.models import User
from ec.views import product_detail


@pytest.mark.django_db
class TestViewsAuthenticated:

    def test_product_detail(self):
        # Create one product
        mixer.blend('ec.Product', pk=1)
        path = reverse('product-detail', kwargs={'pk': 1})

        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        response = product_detail(request, pk=1)
        assert response.status_code == 200

    def test_product_detail_Http404(self):
        path = reverse('product-detail', kwargs={'pk': 1})

        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        with pytest.raises(Http404):
            response = product_detail(request, pk=1)


@pytest.mark.django_db
class TestViewsNotAuthenticated:

    def test_product_detail_will_be_redirected(self):
        # Create one product
        mixer.blend('ec.Product', pk=1)
        path = reverse('product-detail', kwargs={'pk': 1})

        request = RequestFactory().get(path)
        request.user = AnonymousUser()
        response = product_detail(request, pk=1)
        assert response.status_code == 302
        assert '/admin/login/' in response.url
