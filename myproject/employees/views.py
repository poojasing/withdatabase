from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from employees.models import employee
from employees.serializers import EmployeeSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def employees_list(request):
    if request.method == 'GET':
        employees = employee.objects.all()
        firstname = request.GET.get('firstname', None)
        if firstname is not None:
            employees = employees.filter(firstname__icontains=firstname)
        
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse(employees_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(employees_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def employees_detail(request, pk):

    try: 
        emp = employee.objects.get(pk=pk) 
    except employee.DoesNotExist: 
        return JsonResponse({'message': 'The employee does not exist'}, status=status.HTTP_404_NOT_FOUND) 


    if request.method == 'GET': 
        employees_serializer = EmployeeSerializer(emp) 
        return JsonResponse(employees_serializer.data) 
    
    
    elif request.method == 'PUT': 
        employee_data = JSONParser().parse(request) 
        employees_serializer = EmployeeSerializer(emp, data=employee_data) 
        if employees_serializer.is_valid(): 
            employees_serializer.save() 
            return JsonResponse(employees_serializer.data) 
        return JsonResponse(employees_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        emp.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def employees_list_permament(request):
    employees = employee.objects.filter(ispermanent=false)
        
    if request.method == 'GET': 
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)