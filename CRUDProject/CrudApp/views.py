from django.shortcuts import render
from CrudApp.forms import *
from django.core.paginator import  Paginator
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def empview(request):
    if request.method=='GET':
        print('GET Invoked......')
        empform=EmployeeForm()
        return render(request,'CrudApp/addemp.html',{'eform':empform})
    if request.method=='POST':
        print('POST Invoked......')
        empform=EmployeeForm(request.POST)
        if empform.is_valid():
            empform.save()
            return render(request,'CrudApp/msg.html',{'msg':'Registration Success...'})
 #employees=Employee.objects.all().filter(ename__iexact='Amit').order_by('-id')


def homeview(request):
    employees=Employee.objects.all()
    paginator = Paginator(employees, 5)    #total=50  per page =5   1 2 3 4 5 ...10
    page = request.GET.get('page')
    employees = paginator.get_page(page)
    return render(request,'CrudApp/home.html',{'employees':employees})


def email(request):
    subject = 'Django Email Subject'
    message = 'Thank you for register'
    email_from = settings.EMAIL_HOST_USER
   ''''user=form.save();
     uname=user.getUsername()
     user.set_password(user.password)
    recipient_list = [user.email,]'''
    recipient_list = ['ngour@edsystango.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('')






def deleteempview(request,pid):
    emp=Employee.objects.get(id=pid)
    emp.delete()
    return render(request,'CrudApp/msg.html',{'msg':'Deleted Successfully...'})

def updateempview(request,pid):
    emp=Employee.objects.get(id=pid)
    if request.method=='GET':
        return render(request,'CrudApp/update.html',{'emp':emp})
    if request.method=='POST':
        empform=EmployeeForm(request.POST,instance=emp)
        if empform.is_valid():
            empform.save()
            return render(request,'CrudApp/msg.html',{'msg':'Updated Successfully...'})
