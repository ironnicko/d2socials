from django.shortcuts import render
from .models import product
from .forms import productform

# Create your views here.
def create(request, *args, **kwargs):
    if request.method == "GET":
        form = productform()
        context = {"form":form}
        return render(request, "create.html", context)
    if request.method == "POST":
        form = productform(request.POST or None)
        if form.is_valid():
            form.save()
            form = productform()
            context = {"form" : form}
        return render(request, "create.html", context)

    
def view(request, *args, **kwargs):

    # Arrays and Variables 
    
    objects = product.objects.all()
    names = []
    items = []

    # Algorithm to remove repeating submitted form

    for i in objects:
        if i.name.lower() in names:
            index = names.index(i.name.lower())
            product.objects.filter(pk=items[index].id).delete()
        else:
            names.append(i.name.lower())
            items.append(i)
##        product.objects.filter(name="Ananmay").delete()
    context = {'objects': objects}
    return render(request, "view.html", context)

