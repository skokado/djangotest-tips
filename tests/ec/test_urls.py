from django.urls import reverse, resolve


class TestUrls:

    def test_product_detail_url(self):
        path = reverse('product-detail', kwargs={'pk': 1})

        assert path == '/1/'
        assert resolve(path).view_name == 'product-detail'
