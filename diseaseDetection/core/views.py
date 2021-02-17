from django.shortcuts import render,redirect,reverse
from .models import Disease, Category, Symptom, Survey
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "core/template.html")

def home(request):
    return render(request, "core/home.html")


def diseases(request):
    try:
        diseases= Disease.objects.all()
        return render(request, "core/diseases.html", {'diseases': diseases})
    except Exception as e:
        print (e)
        return render(request, "core/home.html")

@login_required
def create_disease(request):
    categories= Category.objects.all()
    symptoms = Symptom.objects.all()
    return render(request, "core/create_disease.html", {"categories" : categories, "symptoms": symptoms})

@login_required
def create(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    symptoms = request.POST.getlist("symptoms")
    try:
        disease = Disease.objects.create(name=name, description=description)
        disease.save()
        for symptom in symptoms:
            s = Symptom.objects.get(name=symptom)
            disease.symptoms.add(s)
    except Exception as e:
        print (e)
    

    return render(request, "core/home.html")

def display(request, id):
    try:
        categories= Category.objects.all()
        disease = Disease.objects.get(id = id)
        return render(request, "core/display.html", {'disease': disease,  'categories': categories})
    except Exception as e:
        print (e)
        return render(request, "core/home.html")

@login_required
def update(request, id):
    
    categories= Category.objects.all()
    disease = Disease.objects.get(id = id)

    if request.method == "GET":
        try:
            return render(request, "core/update.html", {'disease': disease,  'categories': categories})
        except Exception as e:
            print (e)
            return render(request, "core/home.html")

    
    elif request.method == "POST":
        symptoms = request.POST.getlist("symptoms")
        description = request.POST.get("description")
        name = request.POST.get("name")
        try:
            disease.symptoms.clear()
            for symptom in symptoms:
                s = Symptom.objects.get(name=symptom)
                disease.symptoms.add(s)
            disease.description = description
            disease.name = name
            disease.save()
        except Exception as e:
            print (e)
        return redirect(reverse('core:display', kwargs= {'id': id}))


def symptoms(request):
    try:
        symptoms= Symptom.objects.all()
        return render(request, "core/symptoms.html", {'symptoms': symptoms})
    except Exception as e:
        print (e)
        return render(request, "core/home.html")

@login_required
def create_symptom(request, category_id=None):

    categories = Category.objects.all()
    if request.method == "GET":
        return render(request, "core/create_symptom.html", {"categories": categories})
    
    
    elif request.method == "POST":
        try:
            category_instance =request.POST.get("categories")
            category = Category.objects.get(name = category_instance)
            name = request.POST.get("name")
            symptom = Symptom.objects.create(name=name, category=category)
            symptom.save()
        except Exception as e:
            print(e)
        
        return redirect(reverse('core:symptoms'))

@login_required
def newdisease(request):
    if request.method == "GET":
        categories= Category.objects.all()
        symptoms = Symptom.objects.all()
        return render(request, "core/newdisease.html", {"categories" : categories, "symptoms": symptoms})
    elif request.method == "POST":
        diseases= Disease.objects.all()
        name = request.POST.get("name")
        description = request.POST.get("description")
        symptoms = request.POST.getlist("symptoms")
        try:
            disease = Disease.objects.create(name=name, description=description)
            disease.save()
            for symptom in symptoms:
                s = Symptom.objects.get(name=symptom)
                disease.symptoms.add(s)
        except Exception as e:
            print (e)
        

        return render(request, "core/diseases.html", {'diseases': diseases})


@login_required
def create_survey(request, disease_id):
    disease_id = disease_id
    disease = Disease.objects.get(id = disease_id)
    diseases= Disease.objects.all()
    categories= Category.objects.all()
    symptoms = Symptom.objects.all()
    if request.method == "GET":
        return render(request, "core/create_survey.html", {"categories" : categories, "symptoms": symptoms, "disease" : disease})
    elif request.method == "POST":
        description = request.POST.get("description")
        symptoms = request.POST.getlist("symptoms")
        try:
            survey = Survey.objects.create(description=description, disease=disease, user=request.user)
            survey.save()
            for symptom in symptoms:
                s = Symptom.objects.get(name=symptom)
                survey.symptoms.add(s)
        except Exception as e:
            print (e)
        

        return render(request, "core/diseases.html", {'diseases': diseases})

