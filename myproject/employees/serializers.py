from rest_framework import serializers 
from employees.models import employee

class EmployeeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = employee
        fields = (
                 'id',
                'firstname',
                  'lastname',
                  'ispermanent')