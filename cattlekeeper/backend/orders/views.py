from django.shortcuts import render
from .models import Order
from .serializer import OrderSerializer
from shared.decorators import method_required, check_json_body, token_exists, valid_token, user_owner, required_fields
from django.views.decorators.csrf import csrf_exempt
from .helpers import order_exist, product_exist, status_errors, validate_card, valid_status
from products.serializers import ProductSerializer
from django.http import JsonResponse

@csrf_exempt
@method_required('post')
@check_json_body
@valid_token
@token_exists
def add_order(request):
    user = request.user
    order = Order.objects.create(user=user)
    order_json = OrderSerializer(order, request=request)
    return order_json.json_response()

@csrf_exempt
@method_required('get')
@valid_token
@token_exists
@order_exist
@user_owner
def order_product_list(request, order_pk):
    product_json = ProductSerializer(request.order.products.all(), request=request)
    return product_json.json_response()

@csrf_exempt
@method_required('get')
@valid_token
@token_exists
@order_exist
@user_owner
def order_detail(request, order_pk):
    order_json = OrderSerializer(request.order, request=request)
    return order_json.json_response()


@csrf_exempt
@method_required('post')
@check_json_body
@required_fields('product-slug')
@valid_token
@token_exists
@order_exist
@product_exist
@user_owner
def add_game_to_order(request, order_pk):
    order = request.order
    order.add_product(request.product)
    return JsonResponse({'num-products-in-order': order.num_products_in_order()})

@csrf_exempt
@method_required('post')
@check_json_body
@required_fields('status')
@valid_token
@token_exists
@order_exist
@user_owner
@valid_status
@status_errors('cancelled')
def change_order_status(request, order_pk):
    order = request.order
    order.change_status(request.status)
    order.save()
    return JsonResponse({'status': order.get_status_display()})

@csrf_exempt
@method_required('post')
@check_json_body
@required_fields('card-number', 'exp-date', 'cvc')
@valid_token
@token_exists
@order_exist
@csrf_exempt
@user_owner
@status_errors('paid')
@validate_card
def pay_order(request, order_pk):
    order = request.order
    order.change_status(3)
    order.save()
    return JsonResponse({'status': order.get_status_display()})