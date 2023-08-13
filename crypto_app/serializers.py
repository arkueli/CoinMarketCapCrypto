from rest_framework import serializers
from .models import Parser  

class ParserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parser
        fields = '__all__'  




