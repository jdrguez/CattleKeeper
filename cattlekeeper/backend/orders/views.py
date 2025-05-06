from django.shortcuts import render
from .models import Order
from .serializer import OrderSerializer
from shared.decorators import method_required, check_json_body, token_exists, valid_token, user_owner, required_fields
from django.views.decorators.csrf import csrf_exempt
from .helpers import order_exist, product_exist
from products.serializers import ProductSerializer
from django.http import JsonResponse

@csrf_exempt
@method_required('post')
@check_json_body
def add_order(request):
    user = request.user
    order = Order.objects.create(user=user)
    order_json = OrderSerializer(order, request=request)
    return order_json.json_response()

@csrf_exempt
@method_required('get')
@order_exist
@user_owner
def order_product_list(request, order_pk):
    product_json = ProductSerializer(request.order.products.all(), request=request)
    return product_json.json_response()

@csrf_exempt
@method_required('post')
@check_json_body
@required_fields('product-slug')
@order_exist
@product_exist
@user_owner
def add_game_to_order(request, order_pk):
    order = request.order
    order.add_product(request.product)
    return JsonResponse({'num-products-in-order': order.num_products_in_order()})