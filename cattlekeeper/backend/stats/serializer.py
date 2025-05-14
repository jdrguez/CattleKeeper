from shared.serializers import BaseSerializer
from farm.serializers.animals import AnimalBatchSerializer

class MonthlySummarySerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'year': instance.year,
            'month': instance.month,
            'total_income': instance.total_income,
            'total_expense': instance.total_expense,
            'net_profit': instance.net_profit,
            'created_at':instance.created_at.isoformat(),
        }
    
class BatchPerformanceSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'batch': AnimalBatchSerializer(instance.batch, request=self.request).serialize(),
            'period_start': instance.period_start,
            'period_end': instance.period_end,
            'total_production': instance.total_production,
            'total_income': instance.total_income,
            'total_expense': instance.total_expense,
            'created_at':instance.created_at.isoformat(),
        }