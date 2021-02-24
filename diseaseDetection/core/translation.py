from modeltranslation.translator import translator, TranslationOptions
from .models import Category ,Symptom, Disease

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class SymptomTranslationOptions(TranslationOptions):
    fields = ('name',)

class DiseaseTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(Category, CategoryTranslationOptions)
translator.register(Symptom, SymptomTranslationOptions)
translator.register(Disease, DiseaseTranslationOptions)