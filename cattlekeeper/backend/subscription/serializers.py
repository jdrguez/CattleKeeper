from shared.serializers import BaseSerializer

class SubscriptionPlanSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)
    
    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'name': instance.name,
            'price': float(instance.price),
            'duration_days': instance.duration_days,
        }

class UserSubscriptionSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)
    
    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'plan': SubscriptionPlanSerializer(instance.plan, request=self.request).serialize(),
            'start_date': instance.start_date.isoformat(),
            'end_date': instance.end_date.isoformat(),
            'is_active': instance.is_active()
        }
