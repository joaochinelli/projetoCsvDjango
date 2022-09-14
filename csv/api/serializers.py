from rest_framework import serializers
from rest_framework.decorators import action
from csv import models
 
class CsvSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Csv
        fields = '__all__'