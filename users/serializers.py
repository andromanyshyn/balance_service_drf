from rest_framework import serializers
from .models import User


class UserBalanceAddSerializer(serializers.Serializer):
    suma = serializers.DecimalField(max_digits=10, decimal_places=2)
    account_number = serializers.UUIDField()

    def update(self, instance, validated_data):
        instance = User.objects.get(account_number=validated_data.get('account_number'))
        instance.balance += validated_data.get('suma')
        instance.save()
        return instance

    def save(self):
        return self.update(self.instance, self.validated_data)


class UserBalanceSubstractSerializer(serializers.Serializer):
    suma = serializers.DecimalField(max_digits=10, decimal_places=2)
    account_number = serializers.UUIDField()

    @staticmethod
    def validate_balance(instance, validated_data):
        if instance.balance - validated_data.get('suma') < 0:
            raise serializers.ValidationError('suma is greater than your balance')
        return True

    def update(self, instance, validated_data):
        instance = User.objects.get(account_number=validated_data.get('account_number'))
        if self.validate_balance(instance, validated_data):
            instance.balance -= validated_data.get('suma')
            instance.save()
            return instance

    def save(self):
        return self.update(self.instance, self.validated_data)


class UserBalanceSendSerializer(serializers.Serializer):
    from_user = serializers.UUIDField()
    to_user = serializers.UUIDField()
    suma = serializers.DecimalField(max_digits=10, decimal_places=2)

    @staticmethod
    def validate_balance(instance, validated_data):
        if instance.balance - validated_data.get('suma') < 0:
            raise serializers.ValidationError('suma is greater than your balance')
        return True

    def update(self, instance, validated_data):
        from_instance = User.objects.get(account_number=validated_data.get('from_user'))
        to_instance = User.objects.get(account_number=validated_data.get('to_user'))
        if self.validate_balance(from_instance, validated_data):
            from_instance.balance -= validated_data.get('suma')
            to_instance.balance += validated_data.get('suma')

            from_instance.save()
            to_instance.save()
            return from_instance, to_instance

    def save(self):
        return self.update(None, self.validated_data)


class UserBalanceCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'balance',
        )
