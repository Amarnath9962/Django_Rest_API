from rest_framework import serializers
from WebAPP.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        # fields = ("first_name","speciliation","company","experience")
        fields = "__all__"