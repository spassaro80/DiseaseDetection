from django.contrib import admin
from .models import Disease, Symptom, Category, Survey
from modeltranslation.admin import TranslationAdmin

# Register your models here.
class DiseaseAdmin(TranslationAdmin):
    model = Disease

class SymptomAdmin(TranslationAdmin):
    model = Symptom

class CategoryAdmin(TranslationAdmin):
    model = Category

class SurveyAdmin(TranslationAdmin):
    model = Survey

admin.site.register(Disease, TranslationAdmin)
admin.site.register(Symptom,SymptomAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Survey, SurveyAdmin)