from rest_framework import serializers
from .models import Company

from .validators import *

class CompanySerializer(serializers.ModelSerializer):

    company_name = serializers.CharField(validators=[validate_company_name])
    company_code = serializers.CharField(required=False,allow_null=True,allow_blank=True,validators=[validate_company_code])
    strength = serializers.IntegerField(required=False,allow_null=True,validators=[validate_strength])
    class Meta:
        model = Company
        fields = "__all__"
