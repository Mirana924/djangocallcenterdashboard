from django.shortcuts import render

from django.http import HttpResponse
from django import template

# Create your views here.

data = [
    {"User": "yyang", "pwd": "abc"}
]

def index(request):
    global data
    if request.method == "POST":
        data_A = request.POST.get('data_A', None)
        data_B = request.POST.get('data_B', None)
        data_C = request.POST.get('data_C', None)
        temp1 = {"name": "data_A", "int": data_A}
        temp2 = {"name": "data_B", "int": data_B}
        temp3 = {"name": "data_C", "int": data_C}
        data = [temp1, temp2, temp3]
    return render(request, "assigntable/index.html", {"data": data})
