from django.shortcuts import render, HttpResponseRedirect
from .forms import Student_Form
from .models import Student

# Create your views here.
def add_show(request):
    if request.method=="POST":
        form=Student_Form(request.POST)
        if form.is_valid():
            nm=form.cleaned_data['name']
            rn=form.cleaned_data['roll_no']
            em=form.cleaned_data['email']
            ad=form.cleaned_data['address']
            mn=form.cleaned_data['mob_no']
            reg=Student(name=nm, roll_no=rn, email=em, address=ad, mob_no=mn)
            reg.save()
            form=Student_Form()
    else:
        form=Student_Form()
    stud=Student.objects.all()
    context = {"form":form, "stud":stud,}
    return render(request, "testapp/addnshow.html", context )


def update_stud(request, id):
    if request.method=="POST":
        pi=Student.objects.get(pk=id)
        form=Student_Form(request.POST, instance=pi)
        if form.is_valid():
            form.save()

    else:
        pi=Student.objects.get(pk=id)
        form=Student_Form(instance=pi)
    return render(request, "testapp/update.html", {"form":form})


def delete_stud(request, id):
    if request.method=="POST":
        pi=Student.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')
