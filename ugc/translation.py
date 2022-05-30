from modeltranslation.translator import register, TranslationOptions
from .models import Page

@register(Page)
class PageTranslationOptions(TranslationOptions):
  fields = ('title', 'short_description', 'content')