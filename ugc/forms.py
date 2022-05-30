from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):

  class Meta:
    model = Profile
    fields = (
      'name',
    )
    widgets = {
      'name' : forms.TextInput,
    }


class MyFeedbackForm(forms.Form):
  email = forms.EmailField()
  text = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

