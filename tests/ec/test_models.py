from mixer.backend.django import mixer
import pytest

from ec.models import Product


class TestModels:
    @pytest.mark.django_db
    def test_product_is_in_stock(self):
        product = mixer.blend('ec.Product', quantity=1)
        assert product.is_in_stock is True

    @pytest.mark.django_db
    def test_product_is_not_in_stock(self):
        product = mixer.blend('ec.Product', quantity=0)
        assert not product.is_in_stock
