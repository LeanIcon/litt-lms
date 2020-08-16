from rest_framework import serializers

from .models import Lms

class LmsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lms
        fields = ('name', 'alias')