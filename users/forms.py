from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class coustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }
        def __init__(self, *args, **kwargs):
            super(coustomUserCreationForm, self).__init__(*args, **kwargs)
            for name, field in self.fields.items():
                 field.widget.attrs.update({'class': 'input'})
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [ 'name' , 'email', 'username', 'Location', 'bio', 'short_intro', 'Profile_images', 
                  'social_github', 'social_linkedin', 'social_Youtube', 'social_website']
