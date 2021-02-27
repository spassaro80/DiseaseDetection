from modeltranslation.translator import translator, TranslationOptions
from .models import Category ,Symptom, Disease, Survey

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class SymptomTranslationOptions(TranslationOptions):
    fields = ('name',)

class DiseaseTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

class SurveyTranslationOptions(TranslationOptions):
    fields = ('description',)

translator.register(Category, CategoryTranslationOptions)
translator.register(Symptom, SymptomTranslationOptions)
translator.register(Disease, DiseaseTranslationOptions)
translator.register(Survey, SurveyTranslationOptions)