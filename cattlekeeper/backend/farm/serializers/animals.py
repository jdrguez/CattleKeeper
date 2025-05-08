from shared.serializers import BaseSerializer
from accounts.serializers import UserSerializer

class AnimalBatchSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'name': instance.name,
            'slug': instance.slug,
            'species': instance.get_species_display(),
            'purchase_date': instance.purchase_date,
            'sex': instance.get_sex_display(),
            'quantity': instance.quantity,
            'notes': instance.notes,
            'origin': instance.origin,
            'owner': UserSerializer(instance.owner, request=self.request).serialize(),
        }

class AnimalSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'bacth': AnimalBatchSerializer(instance.batch, request=self.request).serialize(),
            'identifier': instance.identifier,
            'slug': instance.slug,
            'birth_date': instance.birth_date,
            'weight': instance.weight,
            'health_status': instance.get_health_status_display(),
            'sex': instance.get_sex_display(),
            'created_at': instance.created_at,
            'notes': instance.notes,
        }