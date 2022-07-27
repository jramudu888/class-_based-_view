from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from django.views.generic import View,TemplateView
#FBV for returning string
def fbv(request):
    return HttpResponse('This FBV function')


#CBV for returning string
class Cbv(View):
    def get(self,request):
        return HttpResponse('CBV first view')

# rendering HTML by using Function Based View

def fbv_template(request):
    return render(request,'fbv_template.html')

# rendering HTML by using Class Based View

class Cbv_template(View):
    def get(self,request):
        d={'name':'Nani','age':10}
        return render(request,'Cbv_template.html',d)

# Dealing with for in Function Based View

def fbv_form(request):
    sf=StudentForm()
    d={'sf':sf}
    if request.method=='POST':
        FD=StudentForm(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))
    return render(request,'fbv_form.html',d)

# dealing with forms in Class based View

class Cbv_form(View):
    def get(self,request):
        sf=StudentForm()
        d={'sf':sf}
        return render(request,'Cbv_form.html',d)


    def post(self,request):
        FD=StudentForm(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))

class Cbv_temp(TemplateView):
    template_name='Cbv_template.html'
