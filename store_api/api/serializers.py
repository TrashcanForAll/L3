from rest_framework.serializers import ModelSerializer
from .models import Token, Good
from rest_framework.serializers import ValidationError

class TokenSerializer(ModelSerializer):

    class Meta:
        model = Token
        fields = '__all__'

class GoodSerializer(ModelSerializer):

    class Meta:
        model = Good
        fields = '__all__'


    def validate_price(self, value):
        if value <= 0:
            raise ValidationError('Price cannot be less zero')
        return value

    def validate_amount(self, value):
        if value < 0:
            raise ValidationError('Amount cannot be negative')
        return value