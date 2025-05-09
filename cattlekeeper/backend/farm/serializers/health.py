from shared.serializers import BaseSerializer
from .animals import AnimalSerializer

class HealthEventSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'animal': AnimalSerializer(instance.animal, request=self.request).serialize(),
            'date': instance.date.isoformat(),
            'event_type': instance.event_type,
            'description': instance.description,
            'veterinarian': instance.veterinarian,
            'created_at':instance.created_at.isoformat(),
        }
