from django import forms
from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields =['title','featured_images','discription','demo_link','source_link','tag']
        widgets  = {
            'tag': forms.CheckboxSelectMultiple(),
        }
    def __init__(self, *args, **kwargs):
            super(ProjectForm, self).__init__(*args, **kwargs)

            self.fields['title'].widget.attrs.update({'class':'input', 'placeholder': 'Add title'})

            self.fields['discription'].widget.attrs.update({'class':'input'})
            self.fields['demo_link'].widget.attrs.update({'class':'input', 'placeholder': 'Add demo-link'})
            self.fields['source_link'].widget.attrs.update({'class':'input', 'placeholder': 'Add source-link'})