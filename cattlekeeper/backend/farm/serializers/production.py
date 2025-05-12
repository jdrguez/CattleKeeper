from shared.serializers import BaseSerializer
from .animals import AnimalBatchSerializer

class ProductionSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'batch': AnimalBatchSerializer(instance.batch, request=self.request).serialize(),
            'production_type': instance.get_production_type_display(),
            'quantity': instance.quantity,
            'unit': instance.get_unit_display(),
            'date': instance.date.isoformat(),
            'notes': instance.notes,
            'created_at':instance.created_at.isoformat(),
        }
