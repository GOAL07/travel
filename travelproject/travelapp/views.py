from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Photos


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1 = Photos.objects.all()
    return render(request,"index.html",{'result':obj, 'image':obj1})

# '''def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse("hello am contact")'''