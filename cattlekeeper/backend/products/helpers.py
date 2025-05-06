from django.http import JsonResponse

from .models import Product, Review, ProductCategory


def product_exist(func):
    def wrapper(request, *args, **kwargs):
        try:
            product = Product.objects.get(slug=kwargs['product-slug'])
            request.product = product
            return func(request,*args, **kwargs)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)

    return wrapper


def review_exist(func):
    def wrapper(request, *args, **kwargs):
        try:
            review = Review.objects.get(pk=kwargs['review_pk'])
            request.review = review
            return func(request,*args, **kwargs)
        except Review.DoesNotExist:
            return JsonResponse({'error': 'Review not found'}, status=404)

    return wrapper