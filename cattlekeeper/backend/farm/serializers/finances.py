from shared.serializers import BaseSerializer
from .animals import AnimalBatchSerializer

class ExpenseSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'batch': AnimalBatchSerializer(instance.batch, request=self.request).serialize(),
            'category': instance.get_category_display(),
            'description': instance.description,
            'amount': instance.amount,
            'currency': instance.get_currency_display(),
            'payment_method': instance.get_payment_method_display(),
            'date': instance.date.isoformat(),
            'created_at':instance.created_at.isoformat(),
        }

class IncomeSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'batch': AnimalBatchSerializer(instance.batch, request=self.request).serialize(),
            'category': instance.get_category_display(),
            'description': instance.description,
            'amount': instance.amount,
            'currency': instance.get_currency_display(),
            'date': instance.date.isoformat(),
            'created_at':instance.created_at.isoformat(),
        }