from datetime import datetime

from django.db.models import Q
from django.shortcuts import render ,HttpResponse
from .models import Department,Role, Employee
def index(request):
    return render(request,'ems_app/index.html')

def addemp(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=request.POST['dept']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        role=request.POST['role']
        phone=int(request.POST['phone'])
        hire_date=request.POST['hire_date']
        new_emp=Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,
                 role_id=role,phone=phone,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully")
    elif request.method=='GET':
        return render(request,'ems_app/addemp.html')

    else :
        return HttpResponse('an exception occured: employee')

def removeemp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('employee removed successsfully')
        except:
            return HttpResponse('please enter a valid emp id.')
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'ems_app/removeemp.html',context)

def filteremp(request):
    if request.method == 'POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains =name) | Q(last_name__icontains = name))
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(role__name__icontains=role)
        context={
            'emps':emps
        }
        return render(request,'ems_app/allemp.html',context)
    elif request.method == 'GET':
        return  render(request,'ems_app/filteremp.html')
    else:
        return HttpResponse('an exception occured')


def allemp(request):
    emp=Employee.objects.all()
    context={
        'emp':emp,
    }
    return render(request,'ems_app/allemp.html',context)

