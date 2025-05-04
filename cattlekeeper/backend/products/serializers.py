from shared.serializers import BaseSerializer
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer

class CategorySerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'name': instance.name,
            'slug': instance.slug,
            'description': instance.description,
            'color': instance.color,
        }
    
class ProductSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance: User) -> dict:
        return {
            'name': instance.name,
            'description': instance.description,
            'price': float(instance.price),
            'category': CategorySerializer(instance.category, request=self.request).serialize(),
            'stock': instance.stock,
            'slug': instance.slug,
            'image': self.build_url(instance.image),
            'created_at': instance.created_at.isoformat(),
        }
    
class ReviewSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'rating': instance.rating,
            'comment': instance.comment,
            'product': ProductSerializer(instance.product, request=self.request).serialize(),
            'author': UserSerializer(instance.author, request=self.request).serialize(),
            'created_at': instance.created_at.isoformat(),
            'updated_at': instance.updated_at.isoformat(),
        }