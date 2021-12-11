from django.shortcuts import render
from .models import People
from .forms import Peopleform

# Create your views here.
def create(request, *args, **kwargs):
    if request.method == "GET":
        form = Peopleform()
        context = {"form":form}
        return render(request, "create.html", context)
    if request.method == "POST":
        form = Peopleform(request.POST or None)
        if form.is_valid():
            form.save()
            form = Peopleform()
            context = {"form" : form}
        return render(request, "create.html", context)

    
def view(request, *args, **kwargs):

    # Arrays and Variables 
    
    objects = People.objects.all()
    names = []
    items = []

    # Algorithm to remove repeating submitted form

    for i in objects:
        if i.name.lower() in names:
            index = names.index(i.name.lower())
            People.objects.filter(pk=items[index].id).delete()
        else:
            names.append(i.name.lower())
            items.append(i)
##        People.objects.filter(name="Ananmay").delete()
    context = {'objects': objects}
    return render(request, "view.html", context)

