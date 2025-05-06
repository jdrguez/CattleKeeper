from products.serializers import ProductSerializer
from shared.serializers import BaseSerializer
from accounts.serializers import UserSerializer


class OrderSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'status': instance.get_status_display(),
            'user': UserSerializer(instance.user, request=self.request).serialize(),
            'key': instance.key if instance.status == 3 else None,
            'products': ProductSerializer(instance.products.all(), request=self.request).serialize(),
            'created_at': instance.created_at.isoformat(),
            'updated_at': instance.updated_at.isoformat(),
            'price': float(instance.price),
        }