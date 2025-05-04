from django.http import JsonResponse
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer
from shared.decorators import method_required, check_json_body, required_fields
from .helpers import product_exist, review_exist
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@method_required('get')
def product_list(request):
    products = Product.objects.all()
    products_json = ProductSerializer(products, request=request)
    return products_json.json_response()

@csrf_exempt
@method_required('get')
@product_exist
def product_detail(request, product_slug):
    product_json = ProductSerializer(request.product, request=request)
    return product_json.json_response()

@csrf_exempt
@method_required('get')
@product_exist
def review_list(request, product_slug):
    reviews = request.product.product_reviews.all()
    review_json = ReviewSerializer(reviews, request=request)
    return review_json.json_response()


@method_required('get')
@review_exist
def review_detail(request, review_pk):
    review_json = ReviewSerializer(request.review, request=request)
    return review_json.json_response()

@csrf_exempt
@method_required('post')
@check_json_body
@required_fields('rating', 'comment')
@product_exist
def add_review(request, product_slug):
    user = request.user
    rating = int(request.json_body['rating'])
    if rating < 1 or rating > 5:
        return JsonResponse({'error': 'Rating is out of range'}, status=400)
    review = Review.objects.create(
        product=request.product,
        author=user,
        rating=rating,
        comment=request.json_body['comment'],
    )
    return JsonResponse({'id': review.pk})