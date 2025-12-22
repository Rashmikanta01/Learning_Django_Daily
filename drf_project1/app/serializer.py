from rest_framework import serializers
from app.models import *

class SchoolMS(serializers.ModelSerializer):
    class Meta:
        model=School
        fields='__all__'