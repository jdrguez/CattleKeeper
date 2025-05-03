from shared.serializers import BaseSerializer
from django.contrib.auth.models import User

class UserSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance: User) -> dict:
        return {
            'id': instance.pk,
            'username': instance.username,
            'email': instance.email,
        }
