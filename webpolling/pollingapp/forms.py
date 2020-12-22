from django import forms
from .models import UserInfoID
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),

)
class UserInfoIDForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    class Meta:
        model = UserInfoID
        fields = "__all__"
        widgets = {
            'gender':forms.RadioSelect(),
            'id_number':forms.NumberInput(attrs={'placeholder':'12-Digit Voter ID.', 'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'placeholder': 'First Name','class':'form-control'}),
            'last_name':forms.TextInput(attrs={'placeholder': 'Last Name', 'class':'form-control'}),
        }
        error_messages = {
            'id_number':{'unique':'Polling has been done through the given voter id. Please vote through other voter id!'}
        }
