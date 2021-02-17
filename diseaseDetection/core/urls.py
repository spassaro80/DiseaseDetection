from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.diseases, name="diseases"),
    path('symptoms/', views.symptoms, name="symptoms"),
    path('', views.home, name="home"),
    path('create', views.create_disease, name="create_disease"),
    path('create_symptom', views.create_symptom, name="create_symptom"),
    path('display/<id>', views.display, name="display"),
    path('created', views.create, name="create"),
    path('update/<id>', views.update, name="update"),
    path('newdisease/', views.newdisease, name="newdisease"),
    path('create_survey/<disease_id>', views.create_survey, name="create_survey"),
    
]