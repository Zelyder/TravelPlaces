from django.contrib import admin
from .forms import ProfileForm
from .models import Profile
from .models import Message
from .models import Page
from modeltranslation.admin import TranslationAdmin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): 
  list_diplay = ('id', 'external_id', 'name')
  form = ProfileForm

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
  list_display = ('id', 'profile', 'text', 'created_at')

@admin.register(Page)
class PageAdmin(TranslationAdmin):
  list_display = ('id', 'title', 'thumbnail_image', 'time_create', 'time_update', 'is_published' )

