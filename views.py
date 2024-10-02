from django.http import HttpResponse, JsonResponse
from .models import Employee, Attendence
from .serializers import EmployeeSerializer, AttendenceSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
import json

def home(request):
    """View to retrieve all employees and return JSON response."""
    employee_data = Employee.objects.all()
    serializer = EmployeeSerializer(employee_data, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def addemployee(request):
    """View to add a new employee."""
    if request.method == 'POST':
        Jsondata = JSONParser().parse(request)

        serializer = EmployeeSerializer(data=Jsondata)
        if serializer.is_valid():
            # Extract validated data
            name = serializer.validated_data.get('name')
            designation = serializer.validated_data.get('designation')
            department = serializer.validated_data.get('department')
            joining_date = serializer.validated_data.get('joining_date')
            email = serializer.validated_data.get('email')
            address = serializer.validated_data.get('address')

        # Check if an employee is already exists
            existing_employee = Employee.objects.filter(name=name,
                                                        designation=designation,
                                                        department=department,
                                                        joining_date=joining_date,
                                                        email=email,
                                                        address=address)

            if existing_employee:
                return JsonResponse({'Already':'employee is already exists.'})
            else:
                serializer.save()

            return JsonResponse({"Employee": "Is add successful"}, status=201)
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def attendence(request):
    """View to mark attendance for an employee."""
    if request.method == 'POST':
        json_data = json.loads(request.body)

        # Extract the employee_name from the JSON data
        name = json_data.get('employee_name', None)
        Department = json_data.get('department', None)

        Jsondata = JSONParser().parse(request)
        serializer = AttendenceSerializer(data=Jsondata)

        if serializer.is_valid():
            # Extract validated data
            date = serializer.validated_data.get('date')
            department = serializer.validated_data.get('department')
            attendence = serializer.validated_data.get('attendence')
            time_in = serializer.validated_data.get('time_in')
            time_out = serializer.validated_data.get('time_out')

            # Retrieve the employee object
            employee = Employee.objects.get(name=name, department=Department)

            # Create and save Attendance instance
            new_attendence = Attendence(date=date,
                                        department=department,
                                        employee=employee,
                                        attendence=attendence,
                                        time_in=time_in,
                                        time_out=time_out)
            new_attendence.save()

            return JsonResponse({"Attendence": "Marked successful"}, status=201)
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def report(request):
    """View to generate a report of the number of employees in each department."""
    department_employee_count = Employee.objects.values('department').annotate(employee_count=Count('id'))
    result_list = list(department_employee_count)

    return JsonResponse(result_list, safe=False)

