from django.shortcuts import redirect, render
from register.forms import *
# Create your views here.
from django.views import View

def showEmpdata(request):
    employee = Employee.objects.all()
    context = {'employee':employee}
    return render(request,'register/show.html',context)

def empRegister(request):

    form = empForm()
    if request.method == "POST":
        form = empForm(request.POST)
        if form.is_valid():
            form.save()
            form = empForm()
    else:

        form = empForm()
    return render(request,'register/add.html',{'form':form})

# =======================================================
# when you click on the edit button that the get request will send, after update when you click on update button
# then form will submit and request will go to POST
def edit(request,id):
    if request.method == "POST":
        gotid = Employee.objects.get(id=id)
        form = empForm(request.POST, instance=gotid)
        if form.is_valid():
            form.save()
    else:
        gotid = Employee.objects.get(id=id)
        form = empForm(instance=gotid)

    return render(request,'register/edit.html',{'form':form})
    # =====================================

def delete(request):
    getId =  request.POST
    # print("key:",getId)
    #THIS METHOD IS USED TO GET DATA FROM FORM
    gotid = getId.get('getid')
    print("value:",gotid)
    delid = Employee.objects.get(id=gotid)
    delid.delete()


    #data delete from database
    # def delete(request,id):
    # if request.method == "POST":
    #     getId = Employee.objects.get(pk = id)
    #     print(getId)
    #     getId.delete()
    return redirect('/')






