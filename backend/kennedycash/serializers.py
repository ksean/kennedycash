from rest_framework import serializers
from . import models


class PersonalTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'date',
            'description',
            'amount',
        )
        model = models.PersonalTransaction
