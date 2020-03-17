from django import forms
lenn=100


BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)
class LogsinForm(forms.Form):
        full_name=forms.CharField(max_length=lenn,widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
	email_id=forms.EmailField(max_length=lenn,widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	password=forms.CharField(  max_length=lenn,widget=forms.PasswordInput(attrs={'placeholder': 'Password'})  )


	
'''
birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
        favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
)
'''
