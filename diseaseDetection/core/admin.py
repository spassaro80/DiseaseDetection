from django.contrib import admin
from .models import Disease, Symptom, Category, Survey

# Register your models here.
class DiseaseAdmin(admin.ModelAdmin):
    model = Disease

class SymptomAdmin(admin.ModelAdmin):
    model = Symptom

class CategoryAdmin(admin.ModelAdmin):
    model = Category

class CategoryAdmin(admin.ModelAdmin):
    model = Survey

admin.site.register(Disease)
admin.site.register(Symptom)
admin.site.register(Category)
admin.site.register(Survey)