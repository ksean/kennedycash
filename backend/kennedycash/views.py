from rest_framework import generics

from . import models
from . import serializers


class ListPersonalTransaction(generics.ListCreateAPIView):
    queryset = models.PersonalTransaction.objects.all()
    serializer_class = serializers.PersonalTransactionSerializer


class DetailPersonalTransaction(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PersonalTransaction.objects.all()
    serializer_class = serializers.PersonalTransactionSerializer
