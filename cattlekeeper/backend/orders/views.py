from django.shortcuts import render
from .models import Order
from .serializer import OrderSerializer
from shared.decorators import method_required, check_json_body
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@method_required('post')
@check_json_body
def add_order(request):
    user = request.user
    order = Order.objects.create(user=user)
    order_json = OrderSerializer(order, request=request)
    return order_json.json_response()

