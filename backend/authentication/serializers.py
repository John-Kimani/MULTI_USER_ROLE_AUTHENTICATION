from rest_framework import serializers
from rest_framework.validators import ValidationError
from phonenumber_field.serializerfields import PhoneNumberField
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    '''
        Create user serializer
    '''

    username=serializers.CharField(max_length=255)
    email=serializers.EmailField(max_length=80)
    phone_number=PhoneNumberField(allow_null=False, allow_blank=False)
    password=serializers.CharField(min_length=8,write_only=True)


    class Meta:
        model = User
        fields = ["email", "username", "phone_number", "password"]

    
    def validate(self, attrs):
        email_exist = User.objects.filter(email=attrs['email']).exists()

        if email_exist:
            raise ValidationError(detail='User with the email provided already exists!')
        
        return super().validate(attrs)