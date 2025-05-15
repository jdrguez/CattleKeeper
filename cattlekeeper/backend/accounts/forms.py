from django import forms

from .models import Profile


from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Nombre",
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label="Apellido",
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Profile
        fields = ['bio', 'avatar']  
        widgets = {
            'avatar': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 20px;',
                    'label': '',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self._user = user  

    def save(self, commit=True):
        profile = super().save(commit=False)

        
        if self._user:
            self._user.first_name = self.cleaned_data.get('first_name', '')
            self._user.last_name = self.cleaned_data.get('last_name', '')
            if commit:
                self._user.save()

        if commit:
            profile.save()
        return profile
