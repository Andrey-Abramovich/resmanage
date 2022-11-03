from rest_framework.serializers import ModelSerializer

from apitest.models import Person


class PersonSerializers(ModelSerializer):
    class Meta:
        model = Person
        fields = ['phone', 'login', 'name', 'birth', 'tg', 'email']


class PersonCreateSerializers(ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
